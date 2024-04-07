from blog.models import Article,Category


def recent_articles(request):
    recent_articles = Article.objects.all().order_by("-created",)
    return {"recent_articles":recent_articles}

def all_categories(request):
    all_categories = Category.objects.all()
    return {"all_categories":all_categories}