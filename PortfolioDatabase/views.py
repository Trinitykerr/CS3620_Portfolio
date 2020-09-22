from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies
# Create your views here.


def home(request):
    context = {}
    return render(request,'PortfolioDatabase/home.html', context)


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request,'PortfolioDatabase/hobbies.html', context)


def portfolio(request):
    p_list = Portfolio.objects.all()
    context = {
        'p_list': p_list,
    }
    return render(request,'PortfolioDatabase/portfoilo.html',context)


def contact(request):
    context = {}
    return render(request,'PortfolioDatabase/contact.html', context)


def details1(request, hobby_id):
    hobby = Hobbies.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'PortfolioDatabase/hdetail.html', context)


def details2(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio':portfolio
    }
    return render(request,'PortfolioDatabase/pdetail.html',context)