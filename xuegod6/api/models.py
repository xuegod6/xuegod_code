from django.db import models
import datetime
# Create your models here.
class BasicUser(models.Model):

    username = models.CharField(max_length=30,verbose_name='用户名')
    password = models.CharField(max_length=30,verbose_name='密码')
    createtime = models.DateField(max_length=30,verbose_name='创建时间',default=datetime.datetime.now())
    class Meta:
        verbose_name = '用户表'

