from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# 21강 회원가입 구현
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# 24강 회원정보
from django.views.generic import DetailView

# 25강 비밀번호 변경
from django.views.generic import UpdateView
from accountapp.forms import AccountUpdateForm

# 26강 계정 삭제
from django.views.generic import DeleteView

# 28강 Decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required

has_ownershp = [account_ownership_required, login_required]

# 41강
from django.views.generic.list import MultipleObjectMixin
from articleapp.models import Article


# Create your views here.

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # reverse / reverse_lazy 차이 함수와 클래스가 파이썬에서 불러와지는 방식이 달라서
    # reverse : 함수 / reverse_lazy : 클래스
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    
    paginate_by = 25
    
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownershp, 'get')
@method_decorator(has_ownershp, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownershp, 'get')
@method_decorator(has_ownershp, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
