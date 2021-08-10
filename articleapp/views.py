from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article

@method_decorator(login_required(login_url=reverse_lazy('popo:login')), 'get')
@method_decorator(login_required(login_url=reverse_lazy('popo:login')), 'post')

# login_required(login_url=reverse_lazy('popo:login') 하는 이유
# : 이게 없으면 기본적으로 장고에서 주는 주소가 accounts/app 이므로 내껀 accountss 이므로 login_url을 바꿔주는 코드를 써야함

class ArticleCreateView(CreateView):

    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'
    # 어떤걸 가지고 할건지

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name =  'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm            # create 폼을 쓴다는 이야기임
    context_object_name = 'target_article'
    template_name =  'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):
    model =Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 1
    # 1페이지에 몇개의 그림을 담을 건지