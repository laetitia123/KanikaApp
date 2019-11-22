from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.contrib.auth.forms import AuthenticationForm
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
from .models import Profile,SpareParts

class RegisterForm(UserCreationForm):
    # email=forms.EmailField()

    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['country'].widget=forms.TextInput()
   class Meta:
       model=Profile
       exclude=['likes']

class sparepartForm(forms.ModelForm):
    class Meta:
        model=SpareParts
        fields=['namePart','price','locationPart','ImagePart','Phone','categoryPart','categoryImage']
