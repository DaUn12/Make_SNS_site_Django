from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from popo.decorators import account_ownership_required
from popo.forms import AccountCreationForm
from popo.models import NewModel

# (login_url= reverse_lazy('accountapp:login'))
# login_url 에 직접적인 주소가 아닌 reverse_lazy로 역추적해서 하면됨
@login_required
# 이거 쓰면 자동적으로 인증과정 됨
def hello_world(request):

    if request.method =='POST':
        # request 함수에 method 라는 저장공간이 있음

        if request.method == 'POST':
            temp = request.POST.get('input_text')
                #  요청정보가 request 로 들어가므로 // input_text 를 불러옴

            new_model = NewModel()  # 변수에 정의한 클래스를 가져옴
            new_model.text = temp
            new_model.save()        # DB에 저장


            # data_list = NewModel.objects.all()
            # 뉴모델 안에있는 모든 값들이 data_list 에 저장됨

            return HttpResponseRedirect(reverse('popo:hello_world'))
            #  이 주소로 가라
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


# accountapp = popo 라고 보자 하고 그 안에 hello_world를 넣는 것 #}

# def hi(request):
#     return HttpResponse('Hello !!')

# 클래스 선언
# 회원가입 로직 만들기
class AccountCreateView(CreateView):
    model = User
    # 계정을 받는거는 특별한 작업이이때문에 장고가 기본적으로 제공해주는 user을 사용
    form_class = UserCreationForm
    # 일반적으로 제공하는sign up 화면폼이라 생각하자

    success_url = reverse_lazy('popo:hello_world')
    # lazy ( urls파일에서의 appname : 우리가 정한 경로 )
    # 회원가입이 성공시 가야하는 url
    # ( 함수에서 불러오는 방식 = reverse // 클래스에서 불러오는 방식 = reverse_lazy)
    # 클래스에서 리버스 쓸때는 에러가 생김

    template_name = 'accountapp/create.html'
    # 여기로 저장한 다는 뜻임 ( 경로 )

class AccountDetailView(DetailView):
    # 장고의 디테일 뷰를 상속받는 클래스를 생성
    model = User
    context_object_name = 'target_user'
    # 상세 계정을 뽑아낼 변수를 추출
    template_name = 'accountapp/detail.html'
    # 상세정보를 할때 어떤 걸로 랜더링할지

has_ownership =[login_required, account_ownership_required]
# 이렇게 할 시 4줄 말고 2줄로 줄일 수 있음
# 4 줄로 할 시
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')



@method_decorator(has_ownership, 'get')    # get 메서드에 해주겟다는 말
@method_decorator(has_ownership, 'post')   # post 메서드에 해주겟다는 말
# 이거 쓰면 함수쓰고 로그인 여부만 확인
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'   # 어떤 객체를 불러올 건지
    # success_url = reverse_lazy('popo:hello_world')
    # 수정 후 어디론가 재연결 할지
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('popo:detail', kwargs={'pk': self.object.pk})
        # popo 자체가 계정앱이기때문에 user를 쓸 필요가 없음
        # object = target_user 이므로
    # 어떤 경로의 html 을 쓸건지


@method_decorator(has_ownership, 'get')        # get 메서드에 해주겟다는말
@method_decorator(has_ownership, 'post')
# 이거 쓰면 함수쓰고 로그인 여부만 확인
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('popo:hello_world')
    template_name = 'accountapp/delete.html'




# 데코레이터 하지 않을 시 방법
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated and self.get_object() == request.user:
#             # 로그인되었을 시
#             return super().get(self, request, *args, **kwargs)
#         # get라는 장고에서 지원하는 객체를 오버라이딩(쌍속) 하여 부모의 것을 받아 그대로 리턴
#
#         else:  # 로그인아닐 시
#             return HttpResponseForbidden()
#         # HttpResponseForbidden() : 금지한다
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated and self.get_object() == request.user:
#             return super().post(self, request, *args, **kwargs)
#         else:
#             return HttpResponseForbidden()
