from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class NewBillForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    start_amount = forms.FloatField()
    interest_rate_date = forms.DateField()

    def clean_interest_rate_date(self):
        data = self.cleaned_data['interest_rate_date']

        # Check if date is in the future
        if data < datetime.today():
            raise ValidationError(_('Invalid Date - interest rate date already passed'))
        return data





