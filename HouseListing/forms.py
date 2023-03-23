from django import forms
from django.forms import widgets
from .models import *
from django.contrib.auth.models import User


class UserLogForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = '__all__'

        widgets = {
            'type': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'type', 'placeholder': 'select type'}),
            'status': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'status', 'placeholder': 'select status'}),
            'city': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'city', 'placeholder': 'select city'}),
            'landsize': forms.Select(attrs={'class': 'form-control custom-select', 'name': 'landsize', 'placeholder': 'select land size'}),
        }



class EditListingForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = '__all__'
        exclude = ['slug', 'user', 'available_rooms',
                   'units', 'default_house_type', 'managed_by_manyumba', 'approved_by_admin', 'featured_image']

        widgets = {
            'type': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'type', 'placeholder': 'select type'}),
            'status': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'status', 'placeholder': 'select status'}),
            'city': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'city', 'placeholder': 'select city'}),
            'landsize': forms.Select(attrs={'class': 'form-control custom-select', 'name': 'landsize', 'placeholder': 'select land size'}),
        }


class ManagePropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = '__all__'

        widgets = {
            'type': forms.Select( attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'type', 'placeholder': 'select type'}),
            'status': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'status', 'placeholder': 'select status'}),
            'city': forms.Select(attrs={'class': 'form-control custom-select', 'required': 'True', 'name': 'city', 'placeholder': 'select city'}),
            'landsize': forms.Select(attrs={'class': 'form-control custom-select', 'name': 'landsize', 'placeholder': 'select land size'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].queryset = PropertyStatus.objects.exclude(
            property_status='For Sale').exclude(property_status='For Lease')


class TenantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['first_name', 'last_name', 'id_number', 'gender', 'email', 'contact',
                  ]


class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = '__all__'

        widgets = {
            'apartment': forms.Select(attrs={'class': 'form-control form-control-select2', 'required': 'True', 'name': 'apartment', 'placeholder': 'Caretaker'}),
            'house': forms.Select(attrs={'class': 'form-control form-control-select2', 'placeholder': 'Caretaker'}),
            'tenant': forms.Select(attrs={'class': 'form-control form-control-select2', 'placeholder': 'Caretaker'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        try:
            user = self.request.user
        except:
            user = None
        self.fields['house'].queryset = House.objects.none()
        self.fields['apartment'].required = True

        self.fields['apartment'].queryset = Properties.objects.filter(user=user,
            managed_by_manyumba=True, approved_by_admin=True)

        if 'apartment' in self.data:
            try:
                apartment_id = int(self.data.get('apartment'))
                self.fields['house'].queryset = House.objects.filter(
                    apartment_id=apartment_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['house'].queryset = self.instance.apartment.house_set.order_by(
                'house_code')

        
