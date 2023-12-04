from django import forms
from django.forms import ModelForm
from .models import MovieCustomUser
from django.contrib.auth.forms import UserCreationForm


# login fields
class LoginForm(ModelForm):
    username = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}),required=True) 
    password = forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model = MovieCustomUser
        fields = ['username', 'password']

# register fields
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'})) 
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={'class':'form-control'}), label= 'Password')

    password2 = forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={'class':'form-control'}), label= 'Confirm Password')
    class Meta:
        model = MovieCustomUser
        fields = ['username', 'email', 'password1', 'password2']

    # to verify whether the two inputted passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1!= password2:
                raise forms.ValidationError('Passwords are not matching')
        return password2

        

        


