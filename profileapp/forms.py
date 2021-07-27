from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
# profileapp- model.py 에있는  profile 이라는 클래스를 받음
        fields = ['image', 'nickname', 'message']

# fields 에서 user 를 안받는 이유는 서버측에서 관리할 것이기 때문에