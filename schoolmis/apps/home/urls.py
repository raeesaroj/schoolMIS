from django.conf.urls import url, include

from apps.home import views
urlpatterns = [
    url(r'^school-create/$', views.SchoolCreateView.as_view(), name='school_create'),
    url(r'^school-list/$', views.SchoolListView.as_view(), name='school_list'),
    url(r'^school-update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='school_update'),
    url(r'^school-delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='school_delete'),

    url(r'^testimonial-create/$', views.TestimonialCreateView.as_view(), name='testimonial_create'),
    url(r'^testimonial-list/$', views.TestimonialListView.as_view(), name='testimonial_list'),
    url(r'^testimonial-update/(?P<pk>\d+)/$', views.TestimonialUpdateView.as_view(), name='testimonial_update'),
    url(r'^testimonial-delete/(?P<pk>\d+)/$', views.TestimonialDeleteView.as_view(), name='testimonial_delete'),

    url(r'^event-create/$', views.EventCreateView.as_view(), name='event_create'),
    url(r'^event-list/$', views.EventListView.as_view(), name='event_list'),
    url(r'^event-detail/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event_detail'),
    url(r'^event-update/(?P<pk>\d+)/$', views.EventUpdateView.as_view(), name='event_update'),
    url(r'^event-delete/(?P<pk>\d+)/$', views.EventDeleteView.as_view(), name='event_delete'),

    url(r'^notice-create/$', views.NoticeCreateView.as_view(), name='notice_create'),
    url(r'^notice-list/$', views.NoticeListView.as_view(), name='notice_list'),
    url(r'^notice-detail/(?P<pk>\d+)/$', views.NoticeDetailView.as_view(), name='notice_detail'),
    url(r'^notice-update/(?P<pk>\d+)/$', views.NoticeUpdateView.as_view(), name='notice_update'),
    url(r'^notice-delete/(?P<pk>\d+)/$', views.NoticeDeleteView.as_view(), name='notice_delete'),

]
