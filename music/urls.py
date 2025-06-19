from django.urls import path
from .views import (
    register,
    CustomLoginView,
    CustomLogoutView,
    dashboard,
    album_list
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('albums/', album_list, name='albums'),  # <-- ВАЖНО: name='albums' как в шаблоне!
]