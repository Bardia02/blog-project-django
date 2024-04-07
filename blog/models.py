from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
# Create your models here.





class Category(models.Model):
    title=models.CharField(max_length=200,verbose_name="موضوع")
    created=models.DateTimeField(auto_now_add=True,verbose_name="ساخته شده در")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="نویسنده")
    category=models.ManyToManyField(Category,verbose_name="دسته بندی")
    title = models.CharField(max_length=100,verbose_name="موضوع")
    body = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to="image/articles",verbose_name="عکس")
    created = models.DateTimeField(auto_now_add=True,verbose_name="ساخته شده در")
    update = models.DateTimeField(auto_now=True,verbose_name="بروز رسانی")
    slug = models.SlugField(null=True,unique=True,blank=True,verbose_name="اسلاگ")
    def get_absolute_url(self):
        # return reverse("blog:post_detail",args=[self.id])
        return reverse("blog:post_detail", args=[self.slug])

    class Meta:
        ordering = ("-created",)
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Article,self).save(args,kwargs)

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        else:
            return format_html('<h3>تصویر ندارد </h3>')
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comments",verbose_name="مقاله")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments",verbose_name="کاربر")
    body = models.TextField(verbose_name="متن وبلاگ")
    created = models.DateTimeField(auto_now_add=True,verbose_name="ساخته شده در")
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies',verbose_name="کامنت")
    def __str__(self):
        return self.body[:20]
    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

class Message(models.Model):
    title = models.CharField(max_length=100,verbose_name="موضوع")
    text = models.TextField(verbose_name="متن")
    email = models.EmailField(verbose_name="ایمیل")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="ساخته شده در")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="likes")
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="likes")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.article.title
    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering=("-created",)




