from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from catalog.models import *
from django.dispatch import receiver
from django.db import IntegrityError
from studentAds.models import ProjectView


def user_logs_in(sender, request, user, **kwargs):
    try:
        LiseliSession.objects.get_or_create(
            user = user,
            session_id = request.session.session_key,
        )
    except (IntegrityError):
        pass

user_logged_in.connect(user_logs_in)

@receiver(post_save, sender=Int_View)
def evaluate_view_count(sender, instance, **kwargs):
    internship = instance.rel_int
    internship.save()

@receiver(post_save, sender=VolView)
def evaluate_vol_view_count(sender,instance,**kwargs):
    volunteer_project=instance.rel_vol
    volunteer_project.save()

@receiver(post_save,sender=ProjectView)
def evaluate_vol_view_count(sender,instance,**kwargs):
    project=instance.rel_project
    project.save()