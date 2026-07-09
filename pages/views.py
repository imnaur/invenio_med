from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView

from pages.models import StaticPage, ContactMessage

from blog.models import Blog
from dotenv import load_dotenv

load_dotenv(override=True)


class StaticPageView(DetailView):
    model = StaticPage
    context_object_name = "page"
    slug_url_kwarg = "page_slug"

    def get_template_names(self):
        if self.object.slug == "contacts":
            return ["pages/contacts.html"]
        elif self.object.slug == "about":
            return ["pages/about_company.html"]
        else:
            return ["pages/homepage.html"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.slug == "contacts":
            email = request.POST.get("email")
            message = request.POST.get("message")
            ContactMessage.objects.create(email=email, message=message)
            try:
                send_mail(
                    subject="Новая заявка с сайта",
                    message=f"От: {email}\n\nСообщение: {message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[
                        "imnaur@bk.ru",
                    ],
                    fail_silently=False,
                )
                messages.success(request, "Ваше сообщение успешно отправлено!")
            except Exception as e:
                print(f"Ошибка отправки: {e}")
                messages.error(request, "Ошибка при отправке почты.")
            return redirect("pages:home")
        return super().get(request, *args, **kwargs)


class HomeTemplateView(TemplateView):
    template_name = "pages/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()[:3]
        return context
