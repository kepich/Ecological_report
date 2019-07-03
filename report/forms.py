from django import forms
from .models import Report 
from django.core.exceptions import ValidationError
import datetime


class ReportForm(forms.ModelForm):
	class Meta():
		model = Report
		fields = ['date', 'place', 'ph', 'comment']

		widgets = {
			'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
			'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Altay Kray, Salt lake'}),
			'ph': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '3.5'}),
			'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your note'}),
		}

		def clean_date(self):
			new_date = 0
			try:
				new_date = datetime.datetime.strptime(self.cleaned_data['date'], '%Y-%m-%d')
			except ValueError:
				raise ValidationError('Incorrect date. Format: YYYY-MM-DD')
			else:
				return self.cleaned_data['date']