from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

# /acounts가 기본값일때  @method_decorator(login_required,'get')

# 그외 일 시
@method_decorator(login_required(login_url=reverse_lazy('popo:login')), 'get')
class SubscriptionView(RedirectView):

    # http 프로토콜에서 get 방식에 대한 처리를 지정
    def get(self, request, *args, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])

        # 구독정보
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        #
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super().get(request, *args, **kwargs)

    # 구독버튼 누르면 다시 게시물 로 넘어가게하는 함수
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': kwargs['project_pk']})


class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    #
    def get_queryset(self):
      # 구독하고 있는 모든 게시판을 가져옴
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
                # values_list('project') : project 만 꺼내오겠다는것
    # 프로젝트 안의 게시물을 가져옴
        article_list = Article.objects.filter(project__in=project_list)
        return article_list
