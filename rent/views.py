from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView

from rent.foms import CompanyForm, ContainerForm
from rent.models import Company, Container


class BaseView(TemplateView):
    template_name = 'rent/base.html'

class CompanyListView(ListView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('rent:base')

class CompanyDetailView(DetailView):
    model = Company

class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('rent:base')

class CompanyDeleteView(DetailView):
    model = Company
    success_url = reverse_lazy('rent:base')

class ContainerListView(ListView):
    model = Container

class ContainerCreateView(CreateView):
    model = Container
    form_class = ContainerForm
    success_url = reverse_lazy('rent:base')

class ContainerDetailView(DetailView):
    model = Container

class ContainerUpdateView(UpdateView):
    model = Container
    form_class = ContainerForm
    success_url = reverse_lazy('rent:base')

class ContainerDeleteView(DetailView):
    model = Container
    success_url = reverse_lazy('rent:base')