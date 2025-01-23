from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

from .tokens import account_activation_token


def forgot_password_email(email, user, reset_link, message, subject):
    send_mail(
        subject,  # subject of email
        message,  # body of email
        settings.DEFAULT_FROM_EMAIL,  # from email
        [
            email,
        ],  # to emails
    )


def user_registration_email(request, user, to_email, password):
    current_site = Site.objects.get_current()
    domain = current_site.domain
    activation_url = reverse(
        "activate",
        kwargs={
            "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        },
    )
    full_activation_url = f"{domain}{activation_url}"
    # activation_url = f"{domain}users/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{account_activation_token.make_token(user)}"
    subject = "Activate your account"
    html_message = render_to_string(
        "users/emails/user_registration_email.html",
        {
            "user": user.username,
            "password": password,
            "domain": domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
            "full_activation_url": full_activation_url,
        },
    )
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [
            to_email,
            settings.DEFAULT_FROM_EMAIL,
        ],
        html_message=html_message,
    )
    if send_mail:
        messages.success(
            request,
            "An email has been sent to your email address. Please check your email to activate your account.",
        )
    else:
        messages.error(
            request,
            "An error occurred while sending the email. Please try again later.",
        )