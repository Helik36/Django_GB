from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import ShopUser
from django.forms import forms


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model: ShopUser
        field = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for filed_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help.text = ''
        def clean_age(self):
            data = self.cleaned_data['age']
            if data < 18:
                raise forms.ValidationError('Вы слишком молоды')
            return data

class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password', 'email', 'age', 'avatar')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for filed_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help.text = ''
                if filed_name == 'password':
                    field.widget = forms.HiddenInput()

        def clean_age(self):
            data = self.cleaned_data['age']
            if data < 18:
                raise forms.ValidationError('Вы слишком молоды')
            return data
