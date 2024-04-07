from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Category,Comment,Message,Like
from django.core.paginator import Paginator
from .forms import ContactUsForm,MessageForm
from django.views.generic.base import View
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoginRequiredMixin
# Create your views here.



def post_detail(request,slug):
    # article=Article.objects.get(id=pk)
    article=get_object_or_404(Article,slug=slug)
    if request.method == "POST":
        body = request.POST.get("body")
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body,article=article,user=request.user,parent_id=parent_id)
    return render(request,"blog/blog_details.html",context={"article":article})

def post_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles,2)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(request , "blog/blog_list.html",context={"articles":object_list})
# class ListView(View):
#     queryset = None
#     template_name = None
#     def get(self,request):
#         return render(request,self.template_name,{'object_list':self.queryset})

class ArticleList(LoginRequiredMixin,ListView):
    queryset = Article.objects.all()
    context_object_name = "articles"
    template_name = 'blog/blog_list.html'
    paginate_by = 2


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/blog_details.html"
    context_object_name = "article"
    slug_field = 'slug'
    slug_url_kwarg = "slug"
    # pk_url_kwarg =
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self.request.user.likes.filter(article__slug=self.object.slug , user_id= self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
            return context
        else:
            return context


    # def post(self,request,slug):
    #     article = get_object_or_404(Article, slug=slug)
    #     body = request.POST.get("body")
    #     parent_id = request.POST.get('parent_id')
    #     Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    #     # return redirect("/")
    #     return render(request, "blog/blog_details.html", context={"article": article})

class ContactUsView(FormView):
    template_name = "blog/contact_us.html"
    form_class = MessageForm
    success_url = "/"
    # reverse_lazy("home:main")
    def form_valid(self, form):
        form_data=form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)
class MessageView(CreateView):
    model = Message
    fields = ("title","email","text")
    success_url = reverse_lazy("home:main")
    template_name = "blog/contact_us.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
    def get_success_url(self):
        print(self.object)
        return super().get_success_url()
# class MessageUpdateView(UpdateView):
#     model = Message
#     fields = ('title','text')
#     template_name = "blog/"


def like(request,slug,pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug,user_id=request.user.id)
            like.delete()
            return JsonResponse({"response": "unliked"})
        except:
            Like.objects.create(article_id=pk,user_id=request.user.id)
            return JsonResponse({"response": "liked"})
    else:
        return redirect("account:login")
    return redirect("blog:post_detail",slug)




def category_detail(request,pk):
    category = get_object_or_404(Category,id=pk)
    articles = category.article_set.all()
    return render(request,"blog/blog_list.html",context={"articles":articles})
def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains=q)
    paginator = Paginator(article,2)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(request,"blog/blog_list.html",{'articles':object_list})


def contact_us(request):
    if request.method =="POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # text = form.cleaned_data.get('text')
            # email = form.cleaned_data.get('email')
            # Message.objects.create(title=title,text=text,email=email)
            form.save(commit=True)
            return redirect("home:main")
    else:
        form = MessageForm()
    return render(request,"blog/contact_us.html",{"form":form})




def test(request):
    print("hiii codeyad")
    return JsonResponse({"response":"liked"})