from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^stajlar/staj-detay/(\d+)',views.internship_detail, name="detay"),
    url(r'^stajlar/', views.internships, name="stajlar"),
    url(r'^company/(\d+)',views.company_detail, name="şirket_detay"),
]