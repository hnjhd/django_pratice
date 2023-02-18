from django.db import models

# Create your models here.
class Major(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name   
class School (models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name
class Country(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name
class Event(models.Model):
    name=models.CharField(verbose_name="名称",max_length=32)
    country=models.ForeignKey(verbose_name="国家",to="Country",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    school=models.ForeignKey(verbose_name="学校",to="School",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    address=models.CharField(verbose_name="参考链接",max_length=32)
    major=models.ForeignKey(verbose_name="专业",to="Major",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
class UserInfo(models.Model):
    name=models.CharField(verbose_name="用户名",max_length=32)
    password=models.CharField(verbose_name="密码",max_length=64)
class UserList(models.Model):
    nid=models.IntegerField(default=0)
    name=models.CharField(verbose_name="名称",max_length=32,default="",null=True)
    country=models.ForeignKey(verbose_name="国家",to="Country",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    school=models.ForeignKey(verbose_name="学校",to="School",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    address=models.CharField(verbose_name="参考链接",max_length=32,default="",null=True)
    major=models.ForeignKey(verbose_name="专业",to="Major",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    uid=models.IntegerField(default=0)