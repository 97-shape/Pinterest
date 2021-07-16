from django.shortcuts import render
from django.urls import reverse_lazy

# 31강

from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'
