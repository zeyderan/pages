from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    #www.site.com
    path('', HomePageView.as_view(), name='home'),
    #www.site.com/about
    path('about', AboutPageView.as_view(), name='about')
]