from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Your Name",
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control bg-light border-0'})
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.TextInput(attrs={'placeholder': 'Your Email', 'class': 'form-control bg-light border-0'})
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control bg-light border-0'})
    )
    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control bg-light border-0',
                'placeholder': 'Leave a message here',
                'style': 'height: 100px',
            })
    )
