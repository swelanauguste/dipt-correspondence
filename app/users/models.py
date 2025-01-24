import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Department(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_creator = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=7, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ["username"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        self.email = self.email.lower()
        self.username = self.username.lower()
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("get-user-detail", kwargs={"slug": self.slug})

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.email}"
