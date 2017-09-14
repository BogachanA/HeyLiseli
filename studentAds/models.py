from django.db import models
from catalog.models import Liseli, HitView
from multiselectfield import MultiSelectField

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
    background_gradient=models.TextField(max_length=1000)

    def __str__(self):
        return "%s" % self.name


class StudentProject(models.Model):
    name=models.CharField(max_length=150)
    owner=models.ForeignKey(Liseli,on_delete=models.CASCADE,related_name='poster')
    description=models.TextField()
    category=models.ForeignKey(ProjectCategory)

    GRADE_CHOICES = (
        ("Prep", "Hazırlık"),
        ("9", "9. sınıf"),
        ("10", "10. sınıf"),
        ("11", "11. sınıf"),
        ("12", "12. sınıf"),
        ("Done", "Liseyi Bitirenler"),
    )
    allowed_grades=MultiSelectField(choices=GRADE_CHOICES)

    required_skills=models.ManyToManyField(RequiredSkill)
    applicants=models.ManyToManyField(Liseli,related_name='applicants',blank=True)

    def __str__(self):
        return "%s" % self.name

class ProjectView(HitView):
    rel_project=models.ForeignKey(StudentProject,related_name='rel_project')