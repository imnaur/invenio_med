from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import (
    RegisterView,
    CustomLoginView,
    CustomUserProfileView,
    CustomUserProfileUpdateView,
)
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="pages:home"), name="logout"),
    path("profile/", CustomUserProfileView.as_view(), name="profile"),
    path(
        "profile/update/", CustomUserProfileUpdateView.as_view(), name="profile_update"
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    # 2. Сообщение: "Письмо отправлено"
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    # 3. Страница с формой нового пароля (открывается по ссылке из письма)
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    # 4. Сообщение: "Пароль успешно изменен"
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
