from django.urls import path
from . import views

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('hobbies/', views.hobbies, name='hobbies'),

    path('portfolio/', views.portfolio, name='portfolio'),

    path('contact/', views.contact, name='contact'),

]
