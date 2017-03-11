#coding=utf-8
import profile

from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from forms import LoginForm, SigninForm, UserForm, ProfileForm
from django.views.generic import View
from models import Profile
from django.contrib.auth.decorators import login_required


class LoginView(View):

    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        username = request.POST.get('usr', '')
        password = request.POST.get('pwd', '')

        form = LoginForm()

        form.usr=username
        form.pwd=password

        #if form.is_valid():
        #username = form.cleaned_data.get('usr', '')
        #password = form.cleaned_data.get('pwd', '')
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append(u"Usuario o contraseña incorrectos")
        else:
            if user.is_active:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)
            else:
                error_messages.append(u"El usuario no está activo")
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('home')



class SigninView(View):
    """Muestra una página que contiene un formulario de inscripción que tiene que
    ser validado manualmente por un administrador.
    """
    def get(self, request):
        success_message = ''
        form = SigninForm()
        context = {
            'form': form,
            'success_message': success_message
        }

        return render(request, 'users/new_user.html', context)

    def post(self, request):
        success_message = ''
        user = User.objects.create_user(request.POST.get('username', ''), request.POST.get('email', ''), request.POST.get('pass', ''))

        user_form = ProfileForm()

        #form = ProfileForm()
        #form.usuario = user_form
        #form.centro = request.POST.get('centro', '')
        #form.responsable = request.POST.get('resp', '')
        #form.fax = request.POST.get('fax', '')

        if user_form.is_valid():
            user.save()

            return redirect('reports/home')
        else:
            success_message = u'¡Guardado con éxito!'

            context = {
                'form': user_form,
                'success_message': success_message
            }

            return render(request, 'users/new_user.html', context)



class ProfileView(View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'profiles/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')

        messages.error(request, _('Please correct the error below.'))