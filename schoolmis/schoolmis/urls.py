"""schoolmis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', include('apps.home.urls', namespace='home')),
    url(r'^api/home/', include('apps.home.api.urls', namespace='home-api')),
    url(r'^admin/', admin.site.urls),
    url(r'^authentication/', include('apps.authentication.urls', namespace='authentication')),
    url(r'^reportcard/', include('apps.reportcard.urls', namespace='reportcard')),
    url(r'^school/', include('apps.school.urls', namespace='school')),
    url(r'^note-assignment/', include('apps.notes.urls', namespace='note_assignment')),
    url(r'^dashboard/', include('apps.dashboard.urls', namespace='dashboard'))
]

urlpatterns.append(url(r'^$', TemplateView.as_view(template_name='index.html')),)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


admin.site.site_header = "GRS User Admin"
admin.site.site_title = "GRS User Admin Portal"
admin.site.index_title = "GRS Site administration"