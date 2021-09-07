from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.models import User ,auth
from django.contrib.auth.decorators import login_required

from App.forms import CompanyForm, EmployeeForm
from App.models import *

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def add_company(request):
    print('fdfjdf')
    if request.method == "POST":

        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})