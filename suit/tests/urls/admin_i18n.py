from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, re_path

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Examples for custom menu
    re_path(r'^admin/', include(admin.site.urls)),
)
