from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, password_validation, login as auth_login, authenticate
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='ID', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), )

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(email=username, password=password)
        if user is not None:
            auth_login(request, user)
            return True
        return False


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'email',
            'last_name',
            'first_name',
            'nickname',
            'img_profile'
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
