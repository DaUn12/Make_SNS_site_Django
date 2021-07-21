from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwarg):
             # 초기화
        super().__init__(*args, **kwarg)
             # super : 부모의 메서드를 가져옴


        self.fields['username'].disabled = True
        # username 이라는 속성을 찾고 비활성화 함(f12 에서 수정해도 그대로임)
        # fields : update 할때의 항목들


#오버라이딩 : 부모의 메서드를 덮어씌움
# 아이디를 비활성화 하게 함
