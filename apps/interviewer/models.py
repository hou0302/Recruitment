from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Interview(models.Model):   # 此处继承AbstractUser， 改写auth_user表，以便登录

    #姓名，选择方向都为必填
    interview_id = models.CharField(max_length=11, verbose_name=u"学号", default='',primary_key=True)
    interview_name = models.CharField(max_length=50, verbose_name=u"姓名", default='')
    interview_direction = models.CharField(max_length=15, verbose_name=u"方向", default='')

    #原因为非必填
    reason = models.TextField (verbose_name=u"原因", null=True, blank=True)

    class Mate:
        verbose_name = '面试官'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.interview_name