from django.db import models

from django.utils import timezone

from extention.utils import JalaliConverter

# Create your models here.

class Catagory(models.Model):
    title=models.CharField(max_length=200,verbose_name='عنوان')
    slug=models.SlugField(max_length=100,verbose_name='عنوان در url')
    status=models.BooleanField(default=True,verbose_name='ایا نمایش داده شود؟')
    position=models.IntegerField(verbose_name='پوزیشن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=['-position']
        

class Article(models.Model):
    STATUS_CHOICES=(
        ('d','پیش نویس'),
        ('p','منتشر شده'),
    )

    title=models.CharField(max_length=200,verbose_name='عنوان')
    slug=models.SlugField(max_length=100,verbose_name='عنوان در url')
    cataogry= models.ManyToManyField(Catagory,verbose_name='دسته بندی')
    description=models.TextField(verbose_name='توضیحات')
    images=models.ImageField(upload_to='images',verbose_name='عکس')
    published=models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    created=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    updated=models.DateTimeField(auto_now=True,verbose_name='تاریخ اپدیت')
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name='حالت')

    def __str__(self):
        return self.title
    
    def Jpublish(self):
        return JalaliConverter(self.published)
        # return self.published
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'