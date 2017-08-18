from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class Liseli(AbstractUser):
    pass

#For the internships
#class Provider


def provider_image_path(instance, filename):
    return '/'.join(['providers',str(instance.id),filename])


class Provider(models.Model):
    company_name=models.CharField(max_length=100)
    company_description=models.TextField(default="")
    company_logo=models.ImageField(upload_to=provider_image_path, default='categories/no-icon.png')
    website=models.URLField(max_length=400,default="none")
    facebook=models.URLField(max_length=400,default="none")
    twitter = models.URLField(max_length=400, default="none")
    linkedin = models.URLField(max_length=400, default="none")
    hq_adress=models.CharField(max_length=400,default="none")
    establishment_date=models.CharField(max_length=40, default="Ezelden beri")
    company_field=models.CharField(max_length=100,default="Firma")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.company_description == "" or not self.company_description:
            self.company_description = self.company_name

        super(Provider, self).save()

    def __str__(self):
        return "%s" % (self.company_name)


def category_image_path(instance, filename):
    return '/'.join(['categories',str(instance.id),filename])


class IntCategory(models.Model):
    name=models.CharField(max_length=200)
    icon=models.ImageField(upload_to=category_image_path,default='categories/no-icon.png')

    def __str__(self):
        return "%s" % (self.name)


def int_cover_image_path(instance, filename):
    return '/'.join(['coverImages',str(instance.id),filename])


class Internship(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(IntCategory)

    TYPE_CHOICES=(
        ("Half & Paid", "Yarı Zamanlı - Maaşlı"),
        ("Half & No", "Yarı Zamanlı - Maaşsız"),
        ("Full & Paid", "Tam Zamanlı - Maaşlı"),
        ("Full & No", "Tam Zamanlı - Maaşsız"),
    )
    type=models.CharField(max_length=200,choices=TYPE_CHOICES,default="Half & No")

    provider=models.ForeignKey(Provider,on_delete=models.CASCADE)
    description=models.TextField()
    requirements=models.TextField()
    date_published=models.DateField(null=True, default=timezone.now)
    location=models.CharField(max_length=200,default="Remote")
    deadline=models.DateField(null=True)
    time_frame=models.CharField(max_length=200,default="Belirli Zaman Yok")
    cover_img=models.ImageField(upload_to=int_cover_image_path,default='categories/no-icon.png')


    def __str__(self):
        return "%s by %s" % (self.name, self.provider)