from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        # meta : 장고에서 지원하는 플랫폼,
        #      : 이미지의 픽셀이 실제데이터인데 외부적인 정보를 정리하는것
        #      : meta 가 있어야 밑에있는 정보를 보여줄 수도 있음
        model = Comment
        fields = ['content']

