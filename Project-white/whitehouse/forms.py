from django import forms
from .widget import DatePickerInput

class AvailabilityForm(forms.Form):
    check_in = forms.DateField(widget=DatePickerInput)
    check_out = forms.DateField(widget=DatePickerInput
    
    )


    



    