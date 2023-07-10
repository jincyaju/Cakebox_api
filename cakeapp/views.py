from django.shortcuts import render,redirect
from cakeapp.models import Cakes
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

from django import forms
# class CakeForm(forms.Form):
#     name=forms.CharField()
#     flavour=forms.CharField()
#     price=forms.IntegerField()
#     shape=forms.CharField()
#     weight=forms.CharField()
#     layer=forms.CharField()
#     description=forms.CharField()

class CakeForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "flavour":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "shape":forms.TextInput(attrs={"class":"form-control"}),
            "weight":forms.TextInput(attrs={"class":"form-control"}),
            "layer":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),

        }

from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","email","username"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

from django.views.generic import View


class CakeCreateView(View):
    def get(self,request,*args,**kw):
        form=CakeForm()
        return render(request,'cake-add.html',{'form':form})
    def post(self,request,*args,**kw):
        form=CakeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cake-list")
        return render(request,'cake-add.html',{"form":form})

class CakeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Cakes.objects.all()
        return render(request,'cake-list.html',{"cakes":qs})
    
class CakeDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cakes.objects.get(id=id)
        return render(request,'cake-detail.html',{'cake':qs})
class CakeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cakes.objects.get(id=id).delete()
        return redirect("cake-list")
    
class CakeEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        ck=Cakes.objects.get(id=id)
        form=CakeForm(instance=ck)
        return render(request,'cake-edit.html',{'form':form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        ck=Cakes.objects.get(id=id)
        form=CakeForm(instance=ck,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cake-detail",pk=id)
        return render(request,'cake-edit.html',{'form':form})
    
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        return render(request,'register.html',{'form':form})
    
    
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("cake-list")
        return render(request,"login.html",{'form':form})
