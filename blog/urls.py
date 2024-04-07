from django.urls import path
from . import views



#start
app_name="blog"
urlpatterns = [
    # path("detail/<int:pk>",views.post_detail,name="post_detail")
    # path("detail/<slug:slug>", views.post_detail, name="post_detail"),
    path("detail/<slug:slug>", views.ArticleDetailView.as_view(), name="post_detail"),
    # path("list", views.post_list, name="post_list"),
    path("category_list/<int:pk>", views.category_detail, name="category_list"),
    path("search", views.search, name="search"),
    # path("contactus",views.contact_us, name='conver'),
    # path("contactus",views.ContactUsView.as_view(), name='conver'),
    path("contactus",views.MessageView.as_view(), name='conver'),
    path("list",views.ArticleList.as_view(),name="post_list"),
    path("like/<slug:slug>/<int:pk>",views.like,name="like"),
    path("test",views.test,name="test")
]