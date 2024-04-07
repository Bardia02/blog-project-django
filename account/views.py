from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import LoginForm,UserEditForm
# Create your views here.

def user_login(request):
    if request.user.is_authenticated == True:
        return redirect("/")

    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get("username"))
            login(request,user)
            return redirect("home:main")
        # username=request.POST.get("username")
        # password=request.POST.get("password")
        # user=authenticate(request,username=username,password=password)
        # if user is not None:
        #     login(request,user)
        #     return redirect('/')
    else:
        form = LoginForm()
    return render(request,"account/login.html",{"form":form})
def user_logout(request):
    logout(request)
    return redirect("/")

def user_register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        user=User.objects.create(username=username,email=email,password=pass2)
        login(request,user)
        return redirect("/")
    return render(request,"account/register.html")


def edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:edit")
    return render(request,"account/edit.html",{"form":form})

