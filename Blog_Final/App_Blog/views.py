#from django.shortcuts import render
#from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.messages.views import SuccessMessageMixin
#from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from App_Blog.models import ModelBlog
#--------------------------------------------------------------
#--------------------------------------------------------------
def homepage(request):
    template = loader.get_template('App_Blog/homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))


class BlogList(ListView):
    model = ModelBlog
    template_name = "App_Blog/notas_list.html"


class BlogDetail(DetailView):
    model = ModelBlog
    template_name = "App_Blog/notas_detail.html"


class BlogCreate(LoginRequiredMixin, CreateView):
    model = ModelBlog
    success_url = reverse_lazy("notas_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ModelBlog
    success_url = reverse_lazy("notas_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]
    def test_func(self):
        exist = ModelBlog.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        

class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = ModelBlog
    success_url = reverse_lazy("notas_list")
    def test_func(self):
        exist = ModelBlog.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'App_Blog/user_login.html'
    next_page = reverse_lazy("notas_list")


class BlogLogout(LogoutView):
    template_name = 'App_Blog/notas_logout.html'