from django.conf.urls import url
from django.contrib import admin

from devices import views as frontend_views

urlpatterns = [
    url(r'^$', frontend_views.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'i13 Demand Manager Admin'
