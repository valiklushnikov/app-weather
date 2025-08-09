from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}
        ),
    )


class RegisterForm(forms.ModelForm):
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={"placeholder": "Email"}
        ),
    )
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
            }
        ),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}
        ),
    )

    password_repeat = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat Password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_repeat"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already in use.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")

        if password and len(password) < 8:
            self.add_error("password", "Password must be at least 6 characters")

        if password and password_repeat and password != password_repeat:
            self.add_error("password_repeat", "Password does not match")
        return cleaned_data


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = ""
        self.fields["email"].widget.attrs.update(
            {"placeholder": "Enter your email"}
        )

    def clean_email(self):
        cd = self.cleaned_data
        if not User.objects.filter(email=cd["email"]).exists():
            raise forms.ValidationError("Email does not exist.")
        return cd["email"]


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].label = ""
        self.fields["new_password2"].label = ""
        self.fields["new_password1"].widget.attrs.update(
            {"placeholder": "New password"}
        )
        self.fields["new_password2"].widget.attrs.update(
            {
                "placeholder": "New password confirmation",
            }
        )
