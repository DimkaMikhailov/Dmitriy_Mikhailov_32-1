from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', min_length=3, max_length=15)
    password = forms.CharField(label='Password', min_length=5, widget=forms.PasswordInput())
    confirm = forms.CharField(label='Confirm Password', min_length=5, widget=forms.PasswordInput())
    im_human = forms.CharField(label="I'm human", widget=forms.CheckboxInput())


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', min_length=3, max_length=15)
    password = forms.CharField(label='Password', min_length=5, widget=forms.PasswordInput())
    im_human = forms.CharField(label="I'm human", widget=forms.CheckboxInput())
