from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(
        label="Contrasena",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Contrasena"
            }
        )
    )
    password2=forms.CharField(
        label="Repetir Contrasena",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Repetir Contrasena"
            }
        )
    )


    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "nombres",
            "apellidos",
            "genero"
        )

    def clean_password2(self):
        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            self.add_error("password2","las contrasenas no son las mismas")
