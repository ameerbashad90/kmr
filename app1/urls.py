from app1.views import kmr1
from django.urls import path
app_name='app1'
urlpatterns=[
    path('kmr1/',kmr1,name='kmr1'),
]