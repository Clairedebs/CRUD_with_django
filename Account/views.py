from django.shortcuts import render
from django.contrib.auth.views import LoginView, redirect_to_login
# Create your views here.
class Login(LoginView):
    template_name='Accountlogin.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return 