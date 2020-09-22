from django.urls import path
from . import views

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('hobbies/<int:hobby_id>', views.details1, name="details1"),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:portfolio_id>', views.details2, name="details2"),
    path('contact/', views.contact, name='contact'),

]
