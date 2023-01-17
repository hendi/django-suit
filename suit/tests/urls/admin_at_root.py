from django.urls import include, re_path
from django.contrib import admin

admin.autodiscover()

urlpatterns =[
    # Examples for custom menu
    re_path(r'^', include(admin.site.urls)),
]
