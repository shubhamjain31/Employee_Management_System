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
    # path('edit/<str:cName>', views.edit ,name='employee_add'),
    # path('update/<str:cName>', views.update ,name='employee_add'),
    # path('delete/<str:cName>', views.delete ,name='employee_add'), 

    # #employee paths
    path('add/employee/', views.add_employee ,name='add_employee'),
    path('show/employee/', views.show_employee ,name='show_employee'),
    # path('deleteEmp/<str:eFname>', views.deleteEmp ,name='employee_add'),
    # path('editemp/<str:eFname>', views.editemp ,name='employee_add'), 
    # path('updateEmp/<str:eFname>', views.updateEmp ,name='employee_add'),
]

#for Media Storage 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 