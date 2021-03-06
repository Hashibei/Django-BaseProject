from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user_email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


class ProfileEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            "email",
            "password"
        )
