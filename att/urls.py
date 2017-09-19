from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name='att'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r"^register/",views.attendancereg,name='att'),
    url(r'^comitteelogin/',views.ulogin,name='auth_login'),
    url(r'^committeeview/',views.attviewauth,name='attviewauth'),
    url(r'^allleavelist/',views.attview,name='attview'),
    url(r'^approve/(?P<attsheet_id>[0-9]+)',views.approveit,name='approveit'),
]