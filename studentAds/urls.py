from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^info/(\d+)/',views.project_details, name="proje_detay"),
    url(r'^$',views.projects_main,name='proje_ana'),
]