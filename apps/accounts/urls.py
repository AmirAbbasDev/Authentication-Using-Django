from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, CustomPasswordResetView, user_logout

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", user_logout, name="logout"),
    path(
        "password/reset/",
        CustomPasswordResetView.as_view(
            template_name="accounts/reset_password/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password/reset/sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/reset_password/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/reset_password/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/reset_password/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
