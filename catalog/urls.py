from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^stajlar/staj-detay/(\d+)/',views.internship_detail, name="detay"),
    url(r'^stajlar/:query=(\w)/',views.internships,name='stajlar_harf'),
    url(r'^stajlar/', views.internships_main, name="stajlar"),
    url(r'^gonullu-projeler/(\d+)', views.volunteer_detail,name='vol_detay'),
    url(r'^gonullu-projeler/:query=(\w)/',views.volunteer_projects,name='vol_harf'),
    url(r'^gonullu-projeler/',views.volunteers,name='vol_ana'),
    url(r'^company/(\d+)/',views.company_detail, name="şirket_detay"),
]