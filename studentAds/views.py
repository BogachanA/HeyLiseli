from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.db import IntegrityError
from django.db.models import Q

# Create your views here.
def project_details(request,project_id):
    project=get_object_or_404(StudentProject, id=project_id)
    try:
        if request.user.is_authenticated():
            view_key=request.user.id
        else:
            if not request.session.get('has_session'):
                request.session['has_session'] = True
            view_key=request.session.session_key

        if not ProjectView.objects.filter(rel_project=project, 
                                      session_key_or_user_id=view_key):
            ProjectView.objects.create(rel_project=project,
                                   session_key_or_user_id=view_key,
                                   date=timezone.now(),
                                   ip=request.META['REMOTE_ADDR'])
    except IntegrityError:
        pass

    current_view_count = ProjectView.objects.filter(rel_project=project).count()
    context={
        'project':project,
    }

    return render(request,'project_detail.html',context)

def projects_main(request):
    categories=ProjectCategory.objects.all()
    top_projects=StudentProject.objects.order_by('-view_count')[:10]
    context={
        'categories':categories,
        'tops':top_projects,
    }
    return render(request,'projects_main.html',context)
