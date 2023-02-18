from django.shortcuts import render,HttpResponse,redirect
from app01.models import UserInfo, Event,School,Country,Major,UserList
from django.core.exceptions import ValidationError
from app01.utils.encrypt import md5
from django import forms 
from django.db import models

class LoginForm(forms.Form):
    name = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True
    )
    def clean_password(self):
        pwd= self.cleaned_data.get("password")
        return md5(pwd)
class UserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label="确认密码",widget=forms.PasswordInput(render_value=True))
    class Meta:
        model = UserInfo
        fields = ["name",'password']
        widgets = {
            "password":forms.PasswordInput(render_value=True)
        }
    def clean_password(self):
        pwd=self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm =md5(self.cleaned_data.get("confirm_password"))
        if confirm!=pwd:
            raise ValidationError("密码不一致")
        return confirm
def register(request):
    if request.method =="GET":
        form=UserModelForm()
        return render(request,'register.html',{'form':form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    return render(request, 'register.html',{'form':form})
def login(request):
    if request.method=="GET":
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        admin_object=UserInfo.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password","用户名或密码错误")
            return render(request,'login.html',{'form':form})
        request.session["info"]= {'id':admin_object.id,'name':admin_object.name}
        return redirect("/event/list")
    return render(request, 'login.html',{'form':form})
def logout(request):
    request.session.clear()
    return redirect('/login')
class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields=["name","country","major","school","address"]
def event_add(request):
    form=EventModelForm()
    if request.method=="GET":
        return render(request,'event_add.html',{"form":form})
    form = EventModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/event/list")
    else: print(form.errors)
def event_list(request):
    data_list=Event.objects.all()
    return render(request,"event_list.html",{"data_list":data_list})
def school_list(request):
    school_list=School.objects.all()
    return render(request,"school_list.html",{"school_list":school_list})
def country_list(request):
    country_list=Country.objects.all()
    return render(request,"country_list.html",{"country_list":country_list})
def major_list(request):
    major_list=Major.objects.all()
    return render(request,"major_list.html",{"major_list":major_list})
def school_add(request):
    if request.method=="GET":
        return render(request,'something_add.html')
    name=request.POST.get("name")
    School.objects.create(name=name)
    return redirect("/event/add")
def country_add(request):
    if request.method=="GET":
        return render(request,'something_add.html')
    name=request.POST.get("name")
    Country.objects.create(name=name)
    return redirect("/event/add")
def major_add(request):
    if request.method=="GET":
        return render(request,'something_add.html')
    name=request.POST.get("name")
    Major.objects.create(name=name)
    return redirect("/event/add")
def event_delete(request):
    nid=request.GET.get('nid')
    Event.objects.filter(id=nid).delete()
    return redirect("/event/list")
def school_delete(request):
    nid=request.GET.get('nid')
    School.objects.filter(id=nid).delete()
    return redirect("/school/list")
def country_delete(request):
    nid=request.GET.get('nid')
    Country.objects.filter(id=nid).delete()
    return redirect("/country/list")
def major_delete(request):
    nid=request.GET.get('nid')
    Major.objects.filter(id=nid).delete()
    return redirect("/major/list")  
def user_event(request):
    nid=request.GET.get('nid')
    eventt=Event.objects.get(id=nid)
    info_dict=request.session["info"]
    uid=info_dict["id"]
    UserList.objects.create(uid=uid,nid=nid,name=eventt.name,address=eventt.address,school=eventt.school,major=eventt.major,country=eventt.country)
    return redirect("/event/list")
def my_event(request):
    info_dict=request.session["info"]
    uid=info_dict["id"]
    my_list=UserList.objects.filter(uid=uid)
    return render(request,'my_event.html',{"my_list":my_list})
def my_event_delete(request):
    nid=request.GET.get('nid')
    UserList.objects.filter(id=nid).delete()
    return redirect("/my_event")
def event_edit(request,nid):
    row_object=Event.objects.filter(id=nid).first()
    if request.method =="GET":
        form=EventModelForm(instance=row_object)
        return render(request,'event_edit.html',{"form":form})
    form = EventModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/event/list/')