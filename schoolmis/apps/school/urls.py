from django.conf.urls import url
from apps.school import views

urlpatterns = [

    url(r'^grade-create/$', views.GradeSubjectSectionCreateView.as_view(), name='grade_create'),
    url(r'^grade-list/$', views.GradeListView.as_view(), name='grade_list'),
    url(r'^grade-update/(?P<slug>[\w-]+)/$', views.GradeSubjectSectionUpdateView.as_view(), name='grade_update'),
    url(r'^grade-detail/(?P<slug>[\w-]+)/$', views.GradeDetailView.as_view(), name='grade_detail'),
    url(r'^grade-delete/(?P<slug>[\w-]+)/$', views.GradeDeleteView.as_view(), name='grade_delete'),

    url(r'^exam-type-create/$', views.ExamTypeCreateView.as_view(), name='exam_type_create'),
    url(r'^exam-type-list/$', views.ExamTypeListView.as_view(), name='exam_type_list'),
    url(r'^exam-type-update/(?P<pk>\d+)/$', views.ExamTypeUpdateView.as_view(), name='exam_type_update'),
    url(r'^exam-type-delete/(?P<pk>\d+)/$', views.ExamTypeDeleteView.as_view(), name='exam_type_delete'),

]
