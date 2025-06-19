from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Album

# Страницы

@login_required
def dashboard(request):
    return render(request, "music/dashboard.html")

@login_required
def album_list(request):
    albums = Album.objects.select_related("artist", "genre").all()
    return render(request, "music/albums.html", {"albums": albums})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'music/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = "music/login.html"

class CustomLogoutView(LogoutView):
    next_page = "login"