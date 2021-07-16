from django.urls import path

# 31강
from profileapp.views import ProfileCreateView
# 32강
from profileapp.views import ProfileUpdateView


app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]