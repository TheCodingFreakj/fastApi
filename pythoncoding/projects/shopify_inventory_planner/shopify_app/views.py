

from django.shortcuts import redirect, render


def home(request):
    print("test view")

    return redirect('http://127.0.0.1:8000/home/')
