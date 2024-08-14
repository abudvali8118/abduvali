from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class LoginUchun(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','kurs','fakultet','username','password1','password2']

