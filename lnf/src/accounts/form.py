from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user do not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
        return super(UserLoginForm,self).clean(*args, **kargs)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    email = forms.EmailField(label= 'Email Address')
    email2 = forms.EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
           'username',
           'email',
           'email2',
           'password',
           ]
    
    def clean(self, *args, **kargs):
        print(self.cleaned_data)
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("Emails didnt match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email already exists")
        
        return super(UserRegisterForm,self).clean(*args, **kargs)



    def clean_email2(self):
        print(self.cleaned_data)
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("Emails didnt match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email already exists")
        
        return email