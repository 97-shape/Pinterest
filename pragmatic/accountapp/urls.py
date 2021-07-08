from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    # 함수형 : 함수_이름
    path('hello_world/', hello_world, name='hello_world'),
    # 클래스형 : 클래스_이름.as_view()
    path('create/', AccountCreateView.as_view(), name='create'),
]