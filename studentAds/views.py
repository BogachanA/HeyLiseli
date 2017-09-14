from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.
def project_details(request,project_id):
    project=get_object_or_404(StudentProject, id=project_id)

    context={
        'project':project,
    }

    return render(request,'project_detail.html',context)