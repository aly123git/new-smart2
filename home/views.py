from django.shortcuts import render, redirect
from django.urls import reverse

#----------------------------------------------------

def home_en(request):
    return render(request, 'home.html',{})

def certificates_en(request):
    return render(request, 'crtf.html',{})


def home_ar(request):
    return render(request, 'home_ar.html',{})

def certificates_ar(request):
    return render(request, 'crtf_ar.html',{})