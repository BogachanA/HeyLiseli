from django.db import models

# Create your models here.

#For the internships
#class Provider
class Provider(models.Model):
    company_name=models.CharField(max_length=100)
    company_description=models.TextField(default="sd")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.company_description == "" or not self.company_description:
            self.company_description = self.company_name

        super(Provider, self).save()


class Internship(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    provider=models.ForeignKey(Provider)
    description=models.TextField()
    requirements=models.TextField()




