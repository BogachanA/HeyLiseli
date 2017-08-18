from django.shortcuts import render, get_object_or_404
from .models import Internship, Provider

# Create your views here.


def internships(request):
    return render(request, 'internship_catalog/internships_main.html')


def internship_detail(request, internship_id):
    internship=get_object_or_404(Internship, id=internship_id)
    context={
        'internship':internship,
    }

    return render(request, 'internship_catalog/internship_details.html',context)


def company_detail(request, company_id):
    company=get_object_or_404(Provider, id=company_id)
    social_links={'facebook':company.facebook,'twitter':company.twitter,'linkedin':company.linkedin}
    context = {
        'company': company,
        'social_links': social_links,
    }
    intset=Internship.objects.filter(provider=company)
    #Volset for volunteer after building the model#
    if intset.exists():
        context['ints_of_comp']=intset

    return render(request,'company_details.html',context)
