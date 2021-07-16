from django.urls import path

# 31강
from profileapp.views import ProfileCreateView


app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
]