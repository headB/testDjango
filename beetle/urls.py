from django.conf.urls import url
from django.contrib import admin

from . import view

urlpatterns = [
    url(r'^beetle$', view.hello),
    url(r'^admin/', admin.site.urls),
]