from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Facts, QNA
from .forms import FactsForm, QNAForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


class Info(TemplateView):
    template_name = "about.html"

class signInFunc(TemplateView):
    template_name = 'signIn.html'

class signUpFunc(TemplateView):
    template_name = 'signUp.html'

class ArticleView(TemplateView):
    template_name = 'article.html'

class CreateFactsView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'article.html'
    form_class = FactsForm
    model = Facts


class FactsUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'article.html'
    form_class = FactsForm
    model = Facts

class CreateQNAView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'article.html'
    form_class = QNAForm
    model = QNA


class QNAUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'article.html'
    form_class = FactsForm
    model = QNA