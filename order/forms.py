from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Select', 'Select'),
		('Nakawa Division', 'Nakawa Division'),
		('Kawempe Division', 'Kawempe Division'),
		('Rubaga Division', 'Rubaga Division'),
		('Makindye Division', 'Makindye Division'),
	)

	DISTRICT_CHOICES = (
		('Select', 'Select'),
		('Kampala', 'Kampala'), 
		('Wakiso', 'Wakiso'),
		('Entebbe', 'Entebbe'),
		('Mukono', 'Mukono'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Cash on Delivery', 'Cash on Delivery'),
		('Moble Money','Moble Money'),
		('VISA','VISA'),
		('Master Card','Master Card'),
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISTRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
