from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms, get_user_model, authenticate, login
from django.views import generic as views
from django.urls import reverse_lazy
from Django_User_and_Password_management.app_auth.forms import UserRegisterForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'user/register-user.html'
    success_url = reverse_lazy('register user')

    # static
    form_class = UserRegisterForm

    # dynamic
    # def get_form_class(self):
    #     pass

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'user/login-user.html'

    # static
    # success_url = reverse_lazy('details user', pk=1)

    # dynamic
    # def get_success_url(self):
    #     pass


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsUserView(views.DetailView):
    model = UserModel
    template_name = 'user/profile-details.html'
