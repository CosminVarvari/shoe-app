from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Manager, Employee, Admin


class ManagerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        manager = Manager.objects.create(user=user)
        manager.phone_number = self.cleaned_data.get('phone_number')
        manager.location = self.cleaned_data.get('location')
        manager.save()
        return user


class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number = self.cleaned_data.get('phone_number')
        employee.designation = self.cleaned_data.get('designation')
        employee.save()
        return user


class AdminSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        admin = Admin.objects.create(user=user)
        admin.phone_number = self.cleaned_data.get('phone_number')
        admin.designation = self.cleaned_data.get('designation')
        admin.save()
        return user


from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'is_employee', 'is_manager', 'is_admin']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_employee': forms.CheckboxInput(),
            'is_manager': forms.CheckboxInput(),
            'is_admin': forms.CheckboxInput(),
        }
        labels = {
            'first_name': 'Enter First Name:',
            'last_name': 'Enter Last Name:',
            'is_employee': 'Is the user employee?',
            'is_manager': 'Is the user manager?',
            'is_admin': 'Is the user admin?',
        }
