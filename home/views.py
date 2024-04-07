from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse , Http404
from blog.models import Article
# Create your views here.
def home(request):
    articles=Article.objects.all()
    # recent = Article.objects.all()[:2]
    recent = Article.objects.all().order_by("-created",)[:2]
    # return reverse("home:main",kwargs={"articles":articles})
    return render(request,"home/index.html",context={"articles":articles,"recent":recent})