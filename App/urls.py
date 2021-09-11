from django.urls import path
from App import views

from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
# from App.views import *

urlpatterns = [
    
    #Homepage path
    path('', views.home, name='home'),

    #Company paths 
    path('add/company/', views.add_company ,name='add_company'),
    path('show/company/', views.show_company ,name='show_company'),
    path('edit/company/<str:cName>', views.edit_company ,name='edit_company'),
    path('delete/company/<str:cName>', views.delete_company ,name='delete_company'), 

    # #employee paths
    path('add/employee/', views.add_employee ,name='add_employee'),
    path('show/employee/', views.show_employee ,name='show_employee'),
    path('delete/employee/<str:eEmail>', views.delete_employee ,name='delete_employee'),
    path('edit/employee/<str:eEmail>', views.edit_employee ,name='edit_employee'),
]

#for Media Storage 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 