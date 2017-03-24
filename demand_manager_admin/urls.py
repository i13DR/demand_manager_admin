from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from devices import views as frontend_views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^$', frontend_views.IndexView.as_view(), name='index'),
    url(r'^crashes/', include('crash.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'i13 Demand Manager Admin'
