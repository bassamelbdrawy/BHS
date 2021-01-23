from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
# from django.contrib.auth import authenticate, login, logout
# from .models import hotels,units,reviews,books,orders,user_information

# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, "gameStore/index.html")