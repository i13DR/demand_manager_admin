from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CrashSubmitView.as_view(), name='submit_crash'),
]
