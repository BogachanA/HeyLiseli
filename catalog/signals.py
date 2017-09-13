from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from catalog.models import LiseliSession, Internship, Liseli, Lise, Int_View
from django.dispatch import receiver
from django.db import IntegrityError


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
    #internship.view_count = IntView.objects.filter(rel_int=internship).count()
    internship.save()
