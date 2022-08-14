from django.urls import URLPattern, path 
from .views import Student_info


urlpatterns=[
    path('api/', Student_info),
]