from django.contrib.auth.forms import AuthenticationForm
from django import forms
from usuario.models import Usuario


class FormularioLogin(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super(FormularioLogin, self)._init_(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    """
    Formulariop de registro de un usuario en al base d3e4 datos
    Variables:
        -password1: Contraseña
        -password2: Verificación de la contraseña

    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Correo electrónico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese su nombre de usuario'

                }
            ),

        }

    def clean_password2(self):
        """
        Esta es la validación de la contraseña
        Este metodo valida que ambas contraseñas sean iguales, antes de ser encriptadas y guardadas en la abse de datos
        Exepciones:
        ValidationError: cuando las contraseñas no son iguales muestra un error
        :return:
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinsiden!')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user
