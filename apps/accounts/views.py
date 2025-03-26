from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout


class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            messages.error(
                self.request, "Ye email registered nahi hai. Pehle account banao."
            )
            return redirect("password_reset")
        return super().form_valid(form)


def user_logout(request):
    logout(request)
    return redirect("login")
