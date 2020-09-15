from django import forms
from .models import Employee



class employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullName', 'emp_code', 'mobile', 'position')
        labels = {
            'fullName':'Full Name',
            'emp_code':'Employee Code',
            'mobile':'Phone No.',
        }

    def __init__(self, *args, **kwargs):
        super(employee_Form, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['position'].required = False
