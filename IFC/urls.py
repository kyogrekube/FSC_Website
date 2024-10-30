"""IFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
admin.autodiscover()
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from IFC import views

urlpatterns = [
    # hook in admin site urls
    path("admin/", admin.site.urls), 

    # IFC app URLs
    path("", views.homepage, name="home"),
    path("documents/", views.documents, name="documents"),
    path("calendar/", views.calendar, name="calendar"),
    path("leadership/", views.leadership, name="leadership"),
    path("recruitment/", views.recruitment, name="recruitment"),
    path("fall/", views.fall, name="fall"),
    path("spring/", views.spring, name="spring"),
    path("event-schedule/", views.eventSchedule, name="event-schedule"),

    path("chapters/", views.ourChapters, name="chapters"),
    path("chapters/<slug:chapter_name>/", views.chapter_detail, name="chapter_detail"),
    path("chapters/<slug:chapter_name>/edit/", views.edit_chapter, name="edit_chapter"),

    path("login/", views.user_login, name="user_login"),
    path("signup/", views.user_signup, name="user_signup"),
    path("logout/", views.user_logout, name="user_logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
