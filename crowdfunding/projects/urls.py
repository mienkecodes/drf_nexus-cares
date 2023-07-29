from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [    
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)# ...from django.contrib import admin- from django.urls import path+ from django.urls import path, includeurlpatterns = [    path('admin/', admin.site.urls),+   path('', include('projects.urls')),]python manage.py runserver
