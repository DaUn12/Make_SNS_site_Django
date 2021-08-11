from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'


    def form_valid(self, form):
        # 댓글작성자 확인 위해
        form.instance.writer = self.request.user
        # articleapp 과 연결
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

    # detail 페이지로 가도록 함
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    # 수행후 어느 페이지로 갈지
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

