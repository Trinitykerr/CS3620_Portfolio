from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies
# Create your views here.


def home(request):
    return HttpResponse("<p>Hi, my name is Trinity Kerr.  I am a junior in the Computer Science program"
                        " at Weber State University. This is a website that I am creating through my"
                        " 3620 class.  I really liked working with web development from the front end, and I am"
                        " excited to learn more about it from the backend.</p>")


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    return HttpResponse(hobby_list)


def portfolio(request):
    p_list = Portfolio.objects.all()
    return HttpResponse(p_list)


def contact(request):
    return HttpResponse("<p>Email: trinitykerr@mail.weber.edu</p>")


# def details1(request, hobby_id):
#     hobby = Hobbies.objects.get(pk=hobby_id)
#     context = {
#         'hobby': hobby
#     }
#     return render(request, 'PortfolioDatabase/hdetail.html', context)


# def details2(request, portfolio_id):
#     portfolio = Portfolio.objects.get(pk=portfolio_id)
#     context = {
#         'portfolio':portfolio
#     }
#     return render(request,'PortfolioDatabase/pdetail.html',context)