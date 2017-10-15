from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session
from django.conf import settings
from random import randint


# Create your models here.


class Lise(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return "%s" % self.name


def user_image_upload_path(instance, filename):
    return "/".join(["UserPhotos", str(instance.id), filename])


def user_resume_upload_path(instance, filename):
    return "resumes/user_{0}/{1}".format(instance.user.username, filename)


class Liseli(AbstractUser):
    summary = models.TextField(max_length=300,
                               default="Sadece benzersiz marjinal bir başka liseliyim. Yerimde duramıyorum aman allahım.")
    lise = models.ForeignKey(Lise, null=True)
    GRADE_CHOICES = (
        ("Choose", "---Sınıfını Seç---"),
        ("Prep", "Hazırlık"),
        ("9", "9. sınıf"),
        ("10", "10. sınıf"),
        ("11", "11. sınıf"),
        ("12", "12. sınıf"),
        ("Done", "Liseyi Bitirdim"),
    )
    GENDERS = (
        ('Choose', '---Cinsiyetin---'),
        ('M', 'Erkek'),
        ('F', 'Kadın'),
        ('N/A', 'Kendimi bu seçeneklerle tanımlamıyorum'),
    )
    grade = models.CharField(max_length=100, choices=GRADE_CHOICES, default="Hazırlık")
    gender = models.CharField(max_length=150, choices=GENDERS, default='Choose')
    user_image = models.ImageField(upload_to=user_image_upload_path, default='categories/no-icon.png', blank=True)
    resume = models.FileField(upload_to=user_resume_upload_path, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.user_image == "categories/no-icon.png" or not self.user_image:
            int = randint(1, 5)
            self.user_image = 'user_pp/user_pp_' + str(int) + '.jpg'

        super(Liseli, self).save()  # TODO look about *args, **kwargs parameters on python and method overriding (pyhon)

    def __str__(self):
        return "%s" % (self.username)


class LiseliSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    session = models.ForeignKey(Session)


# For the internships
def provider_image_path(instance, filename):
    return '/'.join(['providers', str(instance.id), filename])


class Provider(models.Model):
    company_name = models.CharField(max_length=100)
    company_description = models.TextField(default="")
    company_logo = models.ImageField(upload_to=provider_image_path, default='categories/no-icon.png')
    website = models.URLField(max_length=400, default="none")
    facebook = models.URLField(max_length=400, default="none.com")
    twitter = models.URLField(max_length=400, default="none.com")
    linkedin = models.URLField(max_length=400, default="none.com")
    hq_adress = models.CharField(max_length=400, default="none.com")
    establishment_date = models.CharField(max_length=40, default="Ezelden beri")
    company_field = models.CharField(max_length=100, default="Firma")
    apply_email = models.EmailField(max_length=250, null=True)
    contact_email = models.EmailField(max_length=250, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.contact_email == "" or not self.contact_email:
            self.contact_email = self.apply_email

        if self.company_description == "" or not self.company_description:
            self.company_description = self.company_name

        super(Provider, self).save()

    def __str__(self):
        return "%s" % (self.company_name)


def flag_upload_path(instance, filename):
    return '/'.join(['Languages', str(instance.id), filename])


DEFAULT_LANGUAGE_ID = 1


class Language(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to=flag_upload_path, default='categories/no-icon.png')

    def __str__(self):
        return "%s" % self.name


def category_image_path(instance, filename):
    return '/'.join(['categories', str(instance.id), filename])


class IntCategory(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to=category_image_path, default='categories/no-icon.png')

    def __str__(self):
        return "%s" % (self.name)


def int_cover_image_path(instance, filename):
    return '/'.join(['coverImages', str(instance.id), filename])


class Internship(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(IntCategory)

    TYPE_CHOICES = (
        ("Half & Paid", "Yarı Zamanlı - Maaşlı"),
        ("Half & No", "Yarı Zamanlı - Maaşsız"),
        ("Full & Paid", "Tam Zamanlı - Maaşlı"),
        ("Full & No", "Tam Zamanlı - Maaşsız"),
    )
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, default="Half & No")

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    date_published = models.DateField(null=True, default=timezone.now)
    location = models.CharField(max_length=200, default="Remote")
    deadline = models.DateField(null=True)
    time_frame = models.CharField(max_length=200, default="Belirli Zaman Yok")
    cover_img = models.ImageField(upload_to=int_cover_image_path, default='categories/no-icon.png')
    view_count = models.IntegerField(default=0)
    language = models.ForeignKey(Language, null=True, default=DEFAULT_LANGUAGE_ID)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.view_count = Int_View.objects.filter(rel_int=self).count()
        super(Internship, self).save()

    def __str__(self):
        return "%s by %s" % (self.name, self.provider)


class HitView(models.Model):
    date = models.DateTimeField(default=timezone.now)
    ip = models.CharField(max_length=40)
    session_key_or_user_id = models.CharField(max_length=40)

    class Meta:
        abstract = True
        # TODO verbose_name, verbose_name_plural can be setted every model, look META options for model


class Int_View(HitView):
    rel_int = models.ForeignKey(Internship, related_name='InternshipViews')


def vol_category_image_path(instance, filename):
    return '/'.join(['vol_categories', str(instance.id), filename])


def vol_cover_image_path(instance, filename):
    return '/'.join(['VolCoverImages', str(instance.id), filename])


class VolCategory(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to=vol_category_image_path, default='categories/no-icon.png')

    def __str__(self):
        return "%s" % (self.name)


class VolunteerProject(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(VolCategory)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    description = models.TextField()
    responsibilities = models.TextField()
    date_published = models.DateField(null=True, default=timezone.now)
    location = models.CharField(max_length=200, default="Evden")
    deadline = models.DateField(null=True)
    time_frame = models.CharField(max_length=200, default="Yıl İçi")
    cover_img = models.ImageField(upload_to=vol_cover_image_path, default='categories/no-icon.png')
    view_count = models.IntegerField(default=0)
    language = models.ForeignKey(Language, null=True, default=DEFAULT_LANGUAGE_ID)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.view_count = VolView.objects.filter(rel_vol=self).count()
        super(VolunteerProject, self).save()

    def __str__(self):
        return "%s | %s" % (self.name, self.provider)


class VolView(HitView):
    rel_vol = models.ForeignKey(VolunteerProject, related_name='VolunteerViews')
