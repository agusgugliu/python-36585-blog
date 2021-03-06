from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from App_Users.models import Avatar
from App_Users.forms import AvatarForm

###############################################################
###############################################################

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'App_Users/user_create_form.html'
  success_url = reverse_lazy('user_login')
  form_class = UserCreationForm
  success_message = "User created successfully!"





class BloggerProfile(DetailView):
    model = User
    template_name = "App_Users/user_detail.html"





class BloggerUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "App_Users/user_update_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("user_profile", kwargs={"pk": self.request.user.id})





def addAvatar(request):
  if request.method == 'POST':
    form = AvatarForm(request.POST, request.FILES)
    if form.is_valid():
      u = User.objects.get(username=request.user)
      avatar = Avatar(user=u, image=form.cleaned_data['image'])
      avatar.save()
  else:
    form = AvatarForm()
  return render(request, 'App_Users/avatar_form.html', {'form':form})