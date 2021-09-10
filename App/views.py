from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

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
    last = request.META.get('HTTP_REFERER', None)

    if request.method == "POST":
        company_name = request.POST.get('cName')

        if Company.objects.filter(cName__iexact=company_name.strip()).exists():
            messages.error(request, "Company With This Name Already Present")
            return redirect('/add/company')

        form = CompanyForm(request.POST)
        if form.is_valid():
            post        = form.save(commit=False)
            post.user   = request.user

            try:
                post.save()
                messages.success(request, 'Company Added Successfully !')
                return redirect(last)
            except Exception as e:
                print(e)
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})

@login_required(login_url='login')
def edit_company(request, cName):
    last = request.META.get('HTTP_REFERER', None)

    company = get_object_or_404(Company, cName=cName)

    form = CompanyForm(request.POST or None, instance = company)

    if request.method == "POST":
        company_name = request.POST.get('cName')

        all_companies_exclude_same = Company.objects.filter(~Q(cName=cName))
        if all_companies_exclude_same.filter(cName__iexact=company_name).exists():
            messages.error(request, "Company With This Name Already Present")
            return redirect('/edit/company/'+cName)

        if form.is_valid():
            post        = form.save(commit=False)
            post.user   = request.user

            try:
                post.save()
                messages.success(request, 'Company Updated Successfully !')
                return redirect(last)
            except Exception as e:
                print(e)
    else:
        pass
    return render(request, "edit.html", {'form':form})

@login_required(login_url='login')
def show_company(request):
    companies   = Company.objects.all()

    return render(request, "showcompany.html", {'companies':companies})

@login_required(login_url='login')
def delete_company(request, cName):
    last = request.META.get('HTTP_REFERER', None)

    company = Company.objects.get(cName=cName)
    company.delete()

    messages.success(request, 'Company deleted Successfully !')
    return redirect(last)

@login_required(login_url='login')
def add_employee(request):
    last = request.META.get('HTTP_REFERER', None)

    if request.method == "POST":
        employee_email = request.POST.get('eEmail')

        if Employee.objects.filter(eEmail__iexact=employee_email.strip()).exists():
            messages.error(request, "Employee With This Email Already Present")
            return redirect('/add/employee')

        form = EmployeeForm(request.POST)
        if form.is_valid():
            post        = form.save(commit=False)

            try:
                post.save()
                messages.success(request, 'Employee Added Successfully !')
                return redirect(last)
            except Exception as e:
                print(e)
    else:
        form = EmployeeForm()
    return render(request, "employee/addemployee.html", {'form':form})

@login_required(login_url='login')
def show_employee(request):
    employees   = Employee.objects.all()

    return render(request, "employee/showemployee.html", {'employees':employees})

@login_required(login_url='login')
def delete_employee(request, eFname):
    last = request.META.get('HTTP_REFERER', None)

    employee = Employee.objects.get(eFname=eFname)
    employee.delete()

    messages.success(request, 'Employee deleted Successfully !')
    return redirect(last)