from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import request, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

# 원자화 시켜주기 ( 쪼갤 수 없는 하나의 인터랙션 )
@transaction.atomic()
def db_transaction(user, article):
    article.like += 1
    article.save()

    like_record = LikeRecord.objects.filter(user=user, article=article)
    if like_record.exists():
        raise ValidationError('like already exists')    # 장고에서 지원하는 것
        # 검증하는 과정에서 에러시 실행되는 구문
    else:
        # 좋아요가 반영되는 부분
        # n = LikeRecord()
        # n.user = user
        # n.article = article
        # n.save() 의 4줄을 한줄로 함축시켜놓음
        LikeRecord(user=user, article=article).save()
        # DB에 입력



@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):        # 실행후 다시 돌아가야하기때문에 RedirectView

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])
                        # article_pk : urls.py 에서의 path의 pk 이름

        try:
            db_transaction(user, article)
            # 성공시 좋아요 반영됨
            messages.add_message(request, messages.SUCCESS, '좋아요가 반영되었습니다')
        except ValidationError:
             # 실패 시 좋아요 반영 안됨
             messages.add_message(request, messages.ERROR, '좋아요는 한번만가능합니다.')
             return HttpResponseRedirect(reverse('articleapp:detail',
                                                 kwargs={'pk': kwargs['article_pk']}))

        return super().get(request, *args, **kwargs)

    # 실행 시 어디로 갈건지
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail',
                        kwargs={'pk':kwargs['article_pk']})



