from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(requet, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.writer == requet.user:
            return func(requet, *args, **kwargs)

        else:
            return HttpResponseForbidden()

    return decorated()
