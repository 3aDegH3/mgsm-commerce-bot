import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import TimeStampedModel


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    display_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Display name",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        return self.display_name or self.username


class TelegramIdentity(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="telegram_identity",
        verbose_name="User",
    )

    telegram_id = models.BigIntegerField(
        unique=True,
        db_index=True,
        verbose_name="Telegram ID",
    )

    username = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Telegram username",
    )

    first_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="First name",
    )

    last_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Last name",
    )

    language_code = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Language code",
    )

    is_bot = models.BooleanField(
        default=False,
        verbose_name="Is bot",
    )

    raw_data = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="Raw Telegram data",
    )

    class Meta:
        verbose_name = "Telegram identity"
        verbose_name_plural = "Telegram identities"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        if self.username:
            return f"@{self.username}"

        return str(self.telegram_id)