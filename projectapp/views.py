from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    # 객체의 리스트를 돌려줌
    def get_context_data(self, **kwargs):
        # 어떤 유저가 어떤 게시물에 구독했는지 정의 시
        user = self.request.user
        project = self.object  # = target_project 와 같음

        # 로그인 여부 확인
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)
        else:
            subscription = None

        article_list = Article.objects.filter(project=self.object)      # Article = DB
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,
                                        **kwargs)
                        # object_list : 장고에서 지원해주는것


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20
