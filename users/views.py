from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


class LoginPage(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")

            return render(request, self.template_name, {
                'form': form,
            })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(request, username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('/')
