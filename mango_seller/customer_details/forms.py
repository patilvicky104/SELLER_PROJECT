from django import forms
from .models import AddCustomer, Contact


class BillForm(forms.ModelForm):

    class Meta:
        model = AddCustomer
        fields = ("Name", "Phone", 'Buy_kgs',
                  'extra_kgs', 'Rate', 'Bill','Pending')
        widgets = {
            'Name': forms.TextInput(attrs={'type': "Text", 'class': "form-control ", 'id': "Name", 'aria-describedby': "nameHelp", 'placeholder': "Name"}),
            'Phone': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'id': "exampleInputPassword1", 'placeholder': "Mobile Number", }),
            'Buy_kgs': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'id': "amount1", 'placeholder': "Total Buying Kg", }),
            'extra_kgs': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'placeholder': "Extra in Kg", }),
            'Rate': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'id': "amount2", 'placeholder': "Rate", }),
            'Bill': forms.NumberInput(attrs={'type': "number", 'class': "form-control",  'id': "output", 'placeholder': "Total Value", }),
            'Pending': forms.TextInput(attrs={'type': "Text", 'class': "form-control ", 'id': "Name", 'aria-describedby': "nameHelp", 'placeholder': "Name"}),


        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("Name", "contact_number", 'message')
        widgets = {
            'Name': forms.TextInput(attrs={'type': "Text", 'class': "form-control ", 'id': "Name", 'aria-describedby': "nameHelp", 'placeholder': "Name"}),
            'contact_number': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'id': "exampleInputPassword1", 'placeholder': "Mobile Number", }),
            'message': forms.NumberInput(attrs={'type': "textarea", 'class': "form-control", 'id': "amount1", 'placeholder': "Enter your message", }),


        }
