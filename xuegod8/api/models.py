from django.db import models
import datetime
# Create your models here.
class BasicUser(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=20,verbose_name='密码')
    createtime = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    class Meta:
        verbose_name = '用户表'