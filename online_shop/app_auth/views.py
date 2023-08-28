from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login

# Create your views here.

# Создаем отображение профиля
def profile_view(request):
    return render(request, 'app_auth/profile.html')

# Создаем аутентификацию пользователя
def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username, password)
    
    # Проверка, что нашлась комбинация логина и пароля
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    # Комбинация логина и пароля не нашлась - пишем, что пользователь не найден
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})