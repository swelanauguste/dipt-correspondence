import uuid

from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify
from users.models import User


class Incoming(models.Model):
    conf = models.BooleanField("is confidential",default=False)
    urgent = models.BooleanField("is urgent", default=False)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="incoming_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="incoming_updated_by"
    )
    received = models.DateField(default=timezone.now)
    r_from = models.CharField("received from", max_length=255)
    note = models.TextField(blank=True, null=True)
    sender = models.CharField(max_length=255, null=True, blank=True)
    dated = models.DateField()
    subject = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    phone1 = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    file = models.FileField(upload_to="incoming/")

    class Meta:
        ordering = ["-dated"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(Incoming, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("incoming-detail", kwargs={"slug": self.slug})


class IncomingComment(models.Model):
    incoming = models.ForeignKey(
        Incoming, on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incoming_comment_created_by",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incoming_comment_updated_by",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.incoming.incoming_name} - comment {self.pk}"


class Outgoing(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="outgoing_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="outgoing_updated_by"
    )
    add_to = models.CharField("addressed to", max_length=255)
    conf = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="outgoing_sender"
    )
    dated = models.DateField()
    subject = models.CharField(max_length=255)
    file = models.FileField(upload_to="outgoing/")

    class Meta:
        ordering = ["-dated"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(outgoing, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("outgoing-detail", kwargs={"slug": self.slug})


class OutgoingComment(models.Model):
    outgoing = models.ForeignKey(
        Outgoing, on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="outgoing_comment_created_by",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="outgoing_comment_updated_by",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.outgoing.outgoing_name} - comment {self.pk}"
