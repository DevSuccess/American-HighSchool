from django import forms

from Web.utils import STATES


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'})
    )
    age = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Age', 'class': 'form-control'})
    )
    gender = forms.ChoiceField(
        choices=(('male', 'Male'), ('female', 'Female')),
        widget=forms.RadioSelect()
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'})
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'})
    )
    zip_code = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code', 'class': 'form-control'})
    )
    country = forms.ChoiceField(
        choices = STATES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Your message here!', 'class': 'form-control', 'style': 'height: 99px;'})
    )
