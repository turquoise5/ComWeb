"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from comweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query-inclusion/', views.query_inclusion_view, name='query_inclusion'),
    path('query-membership/', views.query_membership, name='query_membership'),
    path('search/class/', views.class_search, name='class_search'),
    path('search/problem/', views.problem_search, name='problem_search'),
    path("ajax/class-search/", views.class_search, name="class_search"),
    path('', views.home, name="home"),    path('machine-info/', views.machine_info_view, name='machine_info'),
    path('complexity-info/', views.complexity_info_view, name='complexity_info'),
    path('inclusions/', views.inclusions_view, name='inclusions'),
    path('mtg/', views.mtg_view, name='mtg'),
    path('mmg/', views.mmg_view, name='mmg'),
    path('problems/', views.problems_view, name='problems'),
    path('memberships/', views.memberships_view, name='memberships'),
    path('nonmemberships/', views.nonmemberships_view, name='nonmemberships'),
    path('noninclusions/', views.noninclusions_view, name='noninclusions'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)