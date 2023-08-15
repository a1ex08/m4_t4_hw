from django.shortcuts import render, redirect
# Подключаем объект для выполнения HTTP-запроса
from django.http import HttpResponse
from .models import OnlineShop
from .forms import AdvertisementForm
from django.urls import reverse

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
    # Проверка на пост запрос
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = OnlineShop(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form':form}
    return render(request, 'advertisement-post.html', context)

def advertisment(request):
    return render(request, 'advertisement.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')
