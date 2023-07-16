from django.db import models

# Create your models here.


class Content(models.Model):

    title = models.CharField('文件名称', max_length=11)
    data = models.FileField(upload_to='data')
    class Meta:
       verbose_name='用户上传文件管理'
       verbose_name_plural=verbose_name




