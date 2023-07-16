from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField('用户名',max_length=32)
    email = models.EmailField('邮箱')
    password = models.CharField('密码',max_length=32)
    class Meta:
       verbose_name='普通用户'
       verbose_name_plural=verbose_name