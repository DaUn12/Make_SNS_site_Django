from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from popo.forms import AccountCreationForm
from popo.models import NewModel


def hello_world(request):

    if request.user.is_authenticated:
        if request.method =='POST':
            # request 함수에 method 라는 저장공간이 있음

            if request.method == 'POST':
                temp = request.POST.get('input_text')
                    #  요청정보가 request 로 들어가므로 // input_text 를 불러옴

                new_model = NewModel()
                new_model.text = temp
                new_model.save()

                # data_list = NewModel.objects.all()
                # 뉴모델 안에있는 모든 값들이 data_list 에 저장됨

                return HttpResponseRedirect(reverse('popo:hello_world'))

                # HttpResponseRedirect  : 해당 주소로 가라
                # reverse('accountapp:hello_world') : 해당 경로를 역변환하여 주소를 찾아냄


        # return  render(request,'accountapp/hello_world.html'
        #                ,context={'new_modeltext':temp })     # 텍스트 창에서 입력한 글자가 바로 밑에 출력이 가능하도록 함
        # HttpResponse 라는 객체를 반환    // 여기에 출력
        # 붉은색 표시일때 alt+enter 눌러서 from.... 누르면 import 할 필요 x


        else:
            data_list = NewModel.objects.all()
            # 뉴모델 안에있는 모든 값들이 data_list 에 저장됨
            return render(request, 'accountapp/hello_world.html'
                          , context={'data_list': data_list})

    else:
        return HttpResponseRedirect(reverse('popo:login'))
# accountapp = popo 라고 보자 하고 그 안에 hello_world를 넣는 것 #}

# def hi(request):
#     return HttpResponse('Hello !!')

# 클래스 선언
# 회원가입 로직 만들기
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('popo:hello_world')
    # lazy ( urls파일에서의 appname : 우리가 정한 경로 )
    # 회원가입이 성공시 가야하는 url
    # ( 함수에서 불러오는 방식 = reverse // 클래스에서 불러오는 방식 = reverse_lazy)
    # 클래스에서 리버스 쓸때는 에러가 생김

    template_name = 'accountapp/create.html'
    # 여기로 저장한 다는 뜻임 ( 경로 )

class AccountDetailView(DetailView):        # 장고의 디테일 뷰를 상속받는 클래스를 생성
    model = User
    context_object_name = 'target_user'  # 상세 계정을 뽑아낼 변수를 추출
    template_name = 'accountapp/detail.html'    # 상세정보를 할때 어떤 걸로 랜더링할지


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('popo:hello_world')
    template_name = 'accountapp/update.html'


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('popo:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('popo:login'))



class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('popo:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('popo:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('popo:login'))
