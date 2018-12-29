from django.db import models

# Create your models here.
class BasicUser(models.Model):

    username = models.CharField(verbose_name='用户名',max_length=20)

    password = models.CharField(verbose_name='密码',max_length=20)

    createTime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

    class Meta:

        verbose_name = '用户表'