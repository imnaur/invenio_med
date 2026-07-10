from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView
from dotenv import load_dotenv

from blog.models import Blog
from pages.models import ContactMessage, StaticPage

load_dotenv(override=True)


class StaticPageView(DetailView):
    """Класс для вывода общей информации в главных страницах"""
    model = StaticPage
    context_object_name = "page"
    slug_url_kwarg = "page_slug"

    def get_template_names(self):
        """Метод выводит по слагу соответствующую страницу"""
        if self.object.slug == "contacts":
            return ["pages/contacts.html"]
        elif self.object.slug == "about":
            return ["pages/about_company.html"]
        else:
            return ["pages/homepage.html"]

    def post(self, request, *args, **kwargs):
        """Метод POST для отправки админам оповещаний об очередной записи"""
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
    """Класс для рендеринга главной страницы"""
    template_name = "pages/homepage.html"

    def get_context_data(self, **kwargs):
        """Метод выводит последние блоги"""
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()[:3]
        return context
