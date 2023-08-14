from django.shortcuts import render
# Подключаем объект для выполнения HTTP-запроса
from django.http import HttpResponse
from .models import OnlineShop

# Create your views here.

# Функция, отображающая index.html
def index(request):
    online_shops = OnlineShop.objects.all()
    context = {'online_shops': online_shops}
    return render(request, 'index.html', context)

# Функция, отображающая top-sellers.html
def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisment_post(request):
    return render(request, 'advertisement-post.html')

def advertisment(request):
    return render(request, 'advertisement.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')