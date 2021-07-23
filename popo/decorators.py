from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request,*args, **kwargs):                              # get에서 받아온 함수를 넣음
        target_user = User.objects.get(pk = kwargs['pk'])               # User의 클래스의 단일 객체를 찾음
        #         pk=kwargs['pk'] : kwargs 의 딕셔너리에서 pk라는걸 찾음

        if target_user == request.user:
            return func(request, *args, **kwargs)
            # get, post 가 값이 있기 때문에 return 시켜줌
        else:
            return HttpResponseForbidden()
            # () : 호출을 하겠다는 뜻 그거 안쓰면 호출이 안됨
    return decorated
