#class based view da render a gerek yok
#from django.shortcuts import render

# import templateview
from django.views.generic import TemplateView

# Create your views here.

#sınıf tabanlı views örneği

#base_dir/templates/pages/home.html yolunu bildirir
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

#base_dir/templates/pages/about.html yolunu bildirir
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

