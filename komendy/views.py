import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Komenda
import re

# Create your views here.

def home(request):
    komendy = []
    for i in Komenda.objects.all(): 
        i.link = i.link.replace(re.sub("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?", '', i.link), '').replace('/watch?v=', '/embed/')
        komendy.append(i)
    data = {
        "list": komendy
    }
    return render(request, "komendy/home.html", data)

def json(request):
    data = list(Komenda.objects.filter(active=True).values())
    return JsonResponse({"data": data})

class CustomLoginView(auth_views.LoginView):
    success_url = "/"
    next_page = "/"
    redirect_authenticated_user = True
    
class CustomLogoutView(auth_views.LogoutView):
    next_page = "/"
    
class KomendaCreateView(LoginRequiredMixin, CreateView):
    model = Komenda
    template_name = "komendy/create_view.html"
    success_url = "/"
    fields = ['name', 'command', 'link', 'volume', 'active']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class KomendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Komenda
    template_name = "komendy/update_view.html"
    success_url = "/"
    fields = ['name', 'command', 'volume', 'active']
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['pk'] = self.kwargs['pk']
        return context
    
class KomendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Komenda
    template_name = "komendy/delete_view.html"
    success_url = "/"
    
    