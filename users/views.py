# websocket info потоки
# Cash
# results -> Doc send to Pat = Pat see / send mail message to email --> Перекидывать на сервисы
# оплата через Stripe -> оплата заранее -3%
# home / нету города, поле поиска, режима работы клиник, услуги выезда на дом, сообщить об ошибке на сайте ,
# футер / услуги клиентам, акции, о компании, справочная
#
# # Упрощенная логика внутри FastAPI
# @app.websocket("/ws/chat")
# async def chat_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         user_input = await websocket.receive_text()
#
#         # 1. Поиск контекста в базе (RAG)
#         context = await db.search_relevant_info(user_input)
#
#         # 2. Формирование промпта
#         prompt = f"Ты помощник клиники. Используй этот контекст: {context}. Ответь: {user_input}"
#
#         # 3. Запрос к ИИ
#         ai_response = await ai_client.chat(prompt)
#
#         # 4. Отправка обратно в чат
#         await websocket.send_text(ai_response)

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import (
    CustomUserAuthenticationForm,
    CustomUserCreationForm,
    CustomUserProfileForm,
)
from .models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("pages:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать!"
        message = "Спасибо за регистрацию на нашем сайте клиники!"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )


class CustomLoginView(LoginView):
    form_class = CustomUserAuthenticationForm
    template_name = "users/login.html"
    success_url = reverse_lazy("pages:home")

    def get_success_url(self):
        return reverse_lazy("pages:home")


class CustomUserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class CustomUserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserProfileForm
    success_url = reverse_lazy("users:profile")
    template_name = "users/profile_update.html"

    def get_object(self, queryset=None):
        return self.request.user
