from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        # Normalize the input for case-insensitivity
        normalized_input = username.strip().lower()

        try:
            # Search for user by username or email (case-insensitive)
            user = User.objects.get(
                Q(username__iexact=normalized_input) | Q(email__iexact=normalized_input)
            )
        except User.DoesNotExist:
            return None

        # Validate the password
        if user.check_password(password):
            return user

        return None