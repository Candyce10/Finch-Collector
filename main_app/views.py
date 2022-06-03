from audioop import reverse
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Finch
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



class Home(View):
    def get(self, request):
        return HttpResponse("Finch Collection")

class About(View):
    def get(self, request):
        return HttpResponse("About")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"



class FinchList(TemplateView):
    template_name= "finch_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for '{name}'"
        else:
            context["finches"] = Finch.objects.filter(user=self.request.user)
            context["header"] = "Finch Gallery"
        return context

class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'habitat', 'food', 'nesting', 'description']
    template_name = "finch_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FinchCreate, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'habitat', 'food', 'nesting', 'description']
    template_name = "finch_update.html"
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDelete(DeleteView):
    model = Finch
    template_name = 'finch_delete.html'
    success_url = '/finchgallery/'

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("finchgallery")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
