
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from User.models import User
from django.shortcuts import HttpResponseRedirect
import hashlib


def setPassword(password):
    """
    加密密码，算法单次md5
    :param apssword: 传入的密码
    :return: 加密后的密码
    """
    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    return str(password)

def register(request):
    if request.method == "POST" and request.POST:
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        User.objects.create(
            username=username,
            email=email,
            password=setPassword(password),
        )
        return HttpResponseRedirect('/login/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST' and request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        e = User.objects.filter(email=email).first()
        if e:
            now_password = setPassword(password)
            db_password = e.password
            if now_password == db_password:
                print(1)
                response = HttpResponseRedirect('/xd/')
                response.set_cookie("username", e.username)
                return response
    return render(request, "login.html")