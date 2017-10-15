from django.shortcuts import render, get_object_or_404
from .models import *
from catalog.forms import applyToInternship
from django.utils import timezone
from django.db import IntegrityError
from django.template.loader import render_to_string
from catalog.helpers import find_recommended_ints
from django.template import Context
from django.core.mail import send_mail, EmailMultiAlternatives
# Create your views here.

def internships_main(request):
     return internships(request,"a")


def internships(request,letter):
    allCategories=IntCategory.objects.all()
    allInts=Internship.objects.all()
    topInts=allInts.order_by('-view_count')[:10]
    valid_letters=[]

    alphabet=('a','b','d','e','f','g','h','i','j','k','l','m','n','p','r','t','v','w','y','z')
    exception_letters={'c':'ç','o':'ö','s':'ş','u':'ü'}
    for k,v in exception_letters.items():
        if allInts.filter(name__istartswith=k).exists() or allInts.filter(name__istartswith=v).exists():
                valid_letters.append(k)
    for i in alphabet:
        if allInts.filter(name__istartswith=i).exists():
            valid_letters.append(i)

    if letter in exception_letters:
        filtered_ints=allInts.filter(name__istartswith=letter) | allInts.filter(name__istartswith=exception_letters[letter])
        filtered_ints=filtered_ints.order_by('name')
    else:
        filtered_ints=allInts.filter(name__istartswith=letter).order_by('name')

    context={
        'categories':allCategories,
        'top_list':topInts,
        'letters':alphabet, #TODO change this to valid_letters
        'letter_ints':filtered_ints,
    }
    return render(request, 'internship_catalog/internships_main.html',context)


def internship_detail(request, internship_id): #TODO add recommended ints by helper functions
    internship=get_object_or_404(Internship, id=internship_id)
    provider = internship.provider
    if request.user.is_authenticated():
        user=request.user
        recommended_ints = find_recommended_ints(internship, request.user)
        if request.method == "GET":
            apply_form = applyToInternship({'name': user.first_name, 'surname': user.last_name, 'school': user.lise.name,'grade':user.grade,'mail':user.email})
    else:
        recommended_ints = find_recommended_ints(internship, user=None)
        apply_form = applyToInternship()

    try:
        if request.user.is_authenticated():
            view_key=request.user.id
        else:
            if not request.session.get('has_session'):
                request.session['has_session'] = True
            view_key=request.session.session_key

        if not Int_View.objects.filter(rel_int=internship,
                                      session_key_or_user_id=view_key):
            Int_View.objects.create(rel_int=internship,
                                   session_key_or_user_id=view_key,
                                   date=timezone.now(),
                                   ip=request.META['REMOTE_ADDR'])
    except IntegrityError:
        pass

    current_view_count = Int_View.objects.filter(rel_int=internship).count()
    context={
        'internship':internship,
        'view_count':current_view_count,
        'recommended':recommended_ints,
    }
    user = request.user
    if request.user.is_authenticated():
        if request.method == "POST":
            apply_form = applyToInternship(request.POST)
            if apply_form.is_valid():
                email_context = Context({
                    'data': apply_form.cleaned_data,
                    'provider': provider,
                    'internship': internship,
                })
                subject = "Yeni bir staj başvurusu"
                from_email = apply_form.cleaned_data['email']
                to_email = provider.apply_email
                text_email = render_to_string('email/application_email.txt', email_context)  # TODO TODOTODOTODOTODO
                html_email = render_to_string('email/application_email.html', email_context)
                msg = EmailMultiAlternatives(subject, text_email, from_email, to_email)
                msg.attach_alternative(html_email, 'text/html')
                msg.content_subtype = 'html'
                msg.send()
                context['success']=True
                return render(request, 'internship_catalog/internship_details.html', context)
    context['apply_form']=apply_form
    return render(request, 'internship_catalog/internship_details.html',context)


def company_detail(request, company_id):
    company=get_object_or_404(Provider, id=company_id)
    social_links={'facebook':company.facebook,'twitter':company.twitter,'linkedin':company.linkedin}
    context = {
        'company': company,
        'social_links': social_links,
    }
    intset=Internship.objects.filter(provider=company)
    # TODO Volset for volunteer after building the model#
    if intset.exists():
        context['ints_of_comp']=intset

    return render(request,'company_details.html',context)


def volunteer_detail(request,volunteer_id):
    project=get_object_or_404(VolunteerProject, id=volunteer_id)
    try:
        if request.user.is_authenticated():
            view_key=request.user.id
        else:
            if not request.session.get('has_session'):
                request.session['has_session'] = True
            view_key=request.session.session_key

        if not VolView.objects.filter(rel_vol=project,
                                      session_key_or_user_id=view_key):
            VolView.objects.create(rel_vol=project,
                                   session_key_or_user_id=view_key,
                                   date=timezone.now(),
                                   ip=request.META['REMOTE_ADDR'])
    except IntegrityError:
        pass

    current_view_count = VolView.objects.filter(rel_vol=project).count()
    context={
        'project':project,
        'view_count':current_view_count,
    }

    return render(request,'volunteer_catalog/volunteer_details.html',context)


def volunteers(request):
    return volunteer_projects(request,"a")

def volunteer_projects(request,letter):
    categories=VolCategory.objects.all()
    topVols=VolunteerProject.objects.order_by('-view_count')[:10]
    allvols=VolunteerProject.objects
    valid_letters = []

    alphabet = ('a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 't', 'v', 'w', 'y', 'z')
    exception_letters = {'c': 'ç', 'o': 'ö', 's': 'ş', 'u': 'ü'}
    for k, v in exception_letters.items():
        if allvols.filter(name__istartswith=k).exists() or allvols.filter(name__istartswith=v).exists():
            valid_letters.append(k)
    for i in alphabet:
        if allvols.filter(name__istartswith=i).exists():
            valid_letters.append(i)

    if letter in exception_letters:
        filtered_vols = allvols.filter(name__istartswith=letter) | allvols.filter(
            name__istartswith=exception_letters[letter])
        filtered_vols = filtered_vols.order_by('name')
    else:
        filtered_vols = allvols.filter(name__istartswith=letter).order_by('name')

    context = {
        'categories': categories,
        'tops': topVols,
        'selected':letter,
        'letters': alphabet,  # TODO change this to valid_letters
        'letter_vols': filtered_vols,
    }
    return render(request,'volunteer_catalog/volunteer_main.html',context)