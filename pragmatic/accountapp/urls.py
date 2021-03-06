from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView
from accountapp.views import AccountUpdateView, AccountDeleteView


# 22강 로그인/아웃

from django.contrib.auth.views import LoginView, LogoutView


app_name = "accountapp"

urlpatterns = [
    # 함수형 : 함수_이름
    # 클래스형 : 클래스_이름.as_view()
    path('create/', AccountCreateView.as_view(), name='create'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

]