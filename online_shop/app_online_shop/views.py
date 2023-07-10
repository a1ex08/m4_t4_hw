from django.shortcuts import render
# Подключаем объект для выполнения HTTP-запроса
from django.http import HttpResponse

# Create your views here.

# Функция, отображающая index.html
def index(request):
    return render(request, 'index.html')
# Функция, отображающая top-sellers.html
def top_sellers(request):
    return render(request, 'top-sellers.html')