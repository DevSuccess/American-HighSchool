from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Your Name",
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.TextInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'})
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'})
    )
    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(
            attrs={'placeholder': 'Your message here!', 'class': 'form-control', 'style': 'height: 99px;'})
    )
