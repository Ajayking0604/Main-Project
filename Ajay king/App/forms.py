from django import forms

class CounterForm(forms.Form):
    increment = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    decrement = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    item_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(widget=forms.HiddenInput)
