from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):        # 실행후 다시 돌아가야하기때문에 RedirectView


    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])
                        # article_pk : urls.py 에서의 path의 pk 이름

        like_record = LikeRecord.objects.filter(user=user, article=article)

        if like_record.exists():     # 좋아요 기록이 있으면 그냥 그 게시물로 다시 되돌아감
            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk':kwargs['article_pk']}))

        else:
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()
        return super().get(request, *args, **kwargs)

    # 실행 시 어디로 갈건지
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail',
                        kwargs={'pk':kwargs['article_pk']})



