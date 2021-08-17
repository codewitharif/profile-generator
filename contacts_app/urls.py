from contacts_app import views
from django.urls import path,include

urlpatterns = [
    path('', views.profile, name='profile'),
    #path('new_profile/', views.new_profile, name='new_profile'),
    
]
