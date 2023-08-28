from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from Django_User_and_Password_management.demo.models import Profile

UserModel = get_user_model()


class UserRegisterForm(auth_forms.UserCreationForm):
    FIRST_NAME_MAX_LENGTH = 30

    consent = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Please enter the same password for verification."),
    )

    first_name = forms.CharField(max_length=FIRST_NAME_MAX_LENGTH, required=True, )

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Please enter the same password.'

    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )

        if commit:
            profile.save()

        return user
