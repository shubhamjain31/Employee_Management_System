from django import forms

from App.models import Employee, Company

# This is for employee
class EmployeeForm(forms.ModelForm):
    eFname = forms.CharField(
        label = 'First Name',
        widget = forms.TextInput(attrs={
            'class':        'form-control',
            'placeholder':  'First Name',
            'rows':          1
        })
    )

    eLname = forms.CharField(
        label = 'Last Name',
        widget = forms.TextInput(attrs={
            'class':        'form-control',
            'placeholder':  'Last Name',
            'rows':          1
        })
    )

    eCompany = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label='-----',
    to_field_name="cName", error_messages={
        'required'              : 'Please Select Company Name',
        'invalid_choice'        : 'Please Select Valid Company',
    },
    widget=forms.Select(
        attrs={
            "placeholder"       : "Company",
            "class"             : "form-control form-control-alternative",
        }
    ))

    eEmail = forms.EmailField(error_messages={
        'required'              : 'Please Enter Company Email',
    },
        widget=forms.EmailInput(
            attrs={
                "placeholder"   : "Employee Email",                
                "class"         : "form-control form-control-alternative"
            }
        ))

    ePhone = forms.CharField(
        label = 'Employee Phone',
        widget = forms.TextInput(attrs={
            'class':        'form-control',
            'placeholder':  'Employee Phone',
            'rows':          1
        })
    )
    
    class Meta:
        model = Employee
        fields = ['eFname', 'eLname', 'eCompany', 'eEmail', 'ePhone']

# This is for company
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