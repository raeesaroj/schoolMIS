from django.conf.urls import url
from apps.home.api import views

urlpatterns = [
    url(r'^testimonial-list/$', views.TestimonialListApiView.as_view(),
        name='testimonial_list'),
    url(r'^school-list/$', views.SchoolListApiView.as_view(), name='school_list'),
    url(r'^event-list/$', views.EventListApiView.as_view(),
        name='testimonial_list'),
    url(r'^notice-list/$', views.NoticeListApiView.as_view(), name='school_list'),
    url(r'^contact/$', views.ContactPostApiView.as_view(), name='contact'),
]
