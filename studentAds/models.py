from django.db import models
from catalog.models import Liseli, HitView, Language,DEFAULT_LANGUAGE_ID
from multiselectfield import MultiSelectField
from django.utils import timezone

# Create your models here.


class RequiredSkill(models.Model):
    skill=models.TextField(max_length=300)

    def __str__(self):
        return "%s" % self.skill


def project_category_upload_path(instance,filename):
    return '/'.join(['StudentProjectCategoryImages',str(instance.id),filename])

class ProjectCategory(models.Model):
    name=models.CharField(max_length=100)
    alpha_icon=models.ImageField(upload_to=project_category_upload_path,default='categories/no-icon.png')
    alpha_icon_2=models.ImageField(upload_to=project_category_upload_path,default='categories/no-icon.png',null=True)
    cover_image=models.ImageField(upload_to=project_category_upload_path,default='categories/no-icon.png')
    background_gradient=models.TextField(max_length=1000)

    def __str__(self):
        return "%s" % self.name


class StudentProject(models.Model):
    name=models.CharField(max_length=150)
    owner=models.ForeignKey(Liseli,on_delete=models.CASCADE,related_name='poster')
    description=models.TextField()
    category=models.ForeignKey(ProjectCategory)
    date_added = models.DateField(null=True, default=timezone.now)
    location = models.CharField(max_length=200, default="Remote")
    project_start = models.DateField(null=True)
    language=models.ForeignKey(Language,default=DEFAULT_LANGUAGE_ID)
    view_count=models.IntegerField(default=0)

    GRADE_CHOICES = (
        ("Prep", "Hazırlık"),
        ("Dokuz", "9. sınıf"),
        ("On", "10. sınıf"),
        ("Onbir", "11. sınıf"),
        ("Oniki", "12. sınıf"),
        ("Done", "Liseyi Bitirenler"),
    )
    allowed_grades=MultiSelectField(choices=GRADE_CHOICES)

    required_skills=models.ManyToManyField(RequiredSkill)
    applicants=models.ManyToManyField(Liseli,related_name='applicants',blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.view_count=ProjectView.objects.filter(rel_project=self).count()
        return super(StudentProject,self).save()

    def __str__(self):
        return "%s" % self.name

class ProjectView(HitView):
    rel_project=models.ForeignKey(StudentProject,related_name='rel_project')