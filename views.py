# coding: utf-8
"""
httf Views
author @alanwikid
"""
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')