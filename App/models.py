from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    cName 		    = models.CharField(primary_key='true',max_length=50,unique='true')
    cEmail 		    = models.EmailField()
    cLogo 		    = models.ImageField(upload_to="images", blank=True)
    cUrl 		    = models.CharField(max_length=50)
    date_created    = models.DateTimeField(auto_now_add=True, null=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.cName

class Employee(models.Model):
    eFname 		   = models.CharField(max_length=50)
    eLname 		   = models.CharField(max_length=50)
    eCompany 	   = models.ForeignKey(Company, on_delete=models.CASCADE)
    eEmail 		   = models.EmailField(primary_key='true', unique='true')
    ePhone 		   = models.CharField(max_length=50)
    date_created   = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.eFname
    
#class Login(models.Model):
    #UserName = models.CharField(max_length=50)
    #password = models.CharField(max_length=32)
    #class Meta:
        #db_table = "login"


