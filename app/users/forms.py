from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "No user is associated with this email address."
            )
        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "department",
            "phone",
        ]


class UserCustomCreationForm(UserCreationForm):
    # allowed_domains = ["gosl.gov.lc", "govt.lc", "gmail.com", "yahoo.com"]

    usable_password = None

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        domain = email.split("@")[-1]

        # # Validate email domain
        # if domain not in self.allowed_domains:
        #     raise forms.ValidationError(
        #         f"Email address must end with one of the allowed domains: {', '.join(self.allowed_domains)}"
        #     )
        # return email

    def clean_username(self):
        # cleaned_data = super().clean()
        email = cleaned_data.get("email")

        # Ensure the username derived from email is unique
        if email:
            username = email.split("@")[0]
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    f"The username '{username}' is already taken. Please use a different email."
                )

        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"].split("@")[
            0
        ]  # Set username based on email
        user.is_active = False  # Set user as inactive by default
        if commit:
            user.save()
        return user
