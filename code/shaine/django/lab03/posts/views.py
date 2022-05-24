from datetime import datetime
from django.shortcuts import render
from .models import Chirp
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ChirpListView(LoginRequiredMixin, ListView):
    model = Chirp
    template_name = 'posts/index.html'
    ordering = ['-datetime']

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model =  Chirp
    
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

class ChirpUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model =  Chirp
    
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        chirp = self.get_object()
        if(self.request.user == chirp.uname):
            return True
        return False

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model =  Chirp
    success_url = '/'

    def test_func(self):
        chirp = self.get_object()
        if(self.request.user == chirp.uname):
            return True
        return False