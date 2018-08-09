from django.conf.urls import url

from apps.dashboard.views import Dashboard

urlpatterns = [
    url(r'^$', Dashboard.as_view(), name='dashboard'),

]
