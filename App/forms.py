from django import forms

from App.models import Employee, Company

# This is for employee
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = "__all__"

#this is for company
class CompanyForm(forms.ModelForm):
    cName = forms.CharField(
        label = 'Customer',
        widget = forms.TextInput(attrs={
            'class':        'form-control',
            'placeholder':  'Company Name',
            'rows':          1
        })
    )

    cEmail = forms.EmailField(error_messages={
        'required'              : 'Please Enter Company Email',
    },
        widget=forms.EmailInput(
            attrs={
                "placeholder"   : "Company Email",                
                "class"         : "form-control form-control-alternative"
            }
        ))

    cLogo = forms.FileField(required=False)

    cUrl = forms.CharField(
        label = 'Customer',
        widget = forms.TextInput(attrs={
            'class':        'form-control',
            'placeholder':  'Company URL',
            'rows':          1
        })
    )
    
    class Meta:
        model = Company
        fields = ['cName', 'cEmail', 'cLogo', 'cUrl']