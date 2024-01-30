from django import forms
from django.core import validators

def validate_for_a(data):
    if data.lower().startswith('a') or data.upper().endswith('@'):
        raise forms.ValidationError('Started with a')

def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('Length is lessthan 5')

class schoolform(forms.Form):
    sname=forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(4)])
    sprincipal=forms.CharField()
    slocation=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('we need to give data in source code')

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        if e!=re:
            raise forms.ValidationError('Mail is invalid or not match')
