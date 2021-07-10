from blog.models import Post
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class SignUpForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2= forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput())
    class Meta:

        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name': 'First Name','last_name' : 'Last Name','email' : 'Email'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs["class"] = "form-control"

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True }))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password' }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs["class"] = "form-control"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
        labels = {'title': 'Title','description':'Description'}

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs["class"] = "form-control"