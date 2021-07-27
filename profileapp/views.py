from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):

    model = Profile
# 어떤모델을 만들 것인지
    form_class = ProfileCreationForm
# 어떤 폼을 사용할 것인지
    success_url = reverse_lazy('popo:hello_world')
# 어디로 되돌아 갈것인지
    template_name = 'profileapp/create.html'
#  어떤 html 파일로 만들것인지

