from django import forms
import datetime

# from django.core import validators
def phone_number(number: str):
    print("a"*100)
    print(number)
    split_number = number.split('-')
    if not len(split_number) == 3:
        if not all([x.isnumeric() for x in split_number]):
            raise forms.ValidationError(f"phone number format xxx-xxx-xxx and integer")
        raise forms.ValidationError(f"phone number must be have - in xxx-xxx-xxx format")


class UserDetails(forms.Form):
    insured_name = forms.CharField(max_length=250)
    insured_job = forms.CharField(max_length=100)
    insured_address = forms.CharField(max_length=100)
    insured_city = forms.CharField(max_length=100)
    insured_state = forms.CharField(max_length=100)
    insured_zip = forms.IntegerField()
    insured_phone = forms.CharField(max_length=150, validators=[phone_number], required=True)
    Created_date = forms.DateTimeField(initial=datetime.datetime.now().strftime('%m/%d/%Y'),
                               disabled=True
                                       )
