from django import forms

class FirstStepForm(forms.Form):
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
