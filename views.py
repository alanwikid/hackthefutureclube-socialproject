# coding: utf-8
"""
httf Views
author @alanwikid
"""
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'vendor/home.html')

def mail(request):
    return redirect('https://www.zoho.com/login.html')