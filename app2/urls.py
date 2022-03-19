from app2.views import kmr2
from django.urls import path
app_name='app2'
urlpatterns=[
    path('kmr2/',kmr2,name='kmr2'),
]