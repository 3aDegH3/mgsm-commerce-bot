from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import TelegramIdentity, User


class TelegramIdentityInline(admin.StackedInline):
    model = TelegramIdentity
    extra = 1
    max_num = 1
    can_delete = True

    fields = (
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "language_code",
        "is_bot",
    )


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    inlines = (TelegramIdentityInline,)

    list_display = (
        "username",
        "display_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )

    search_fields = (
        "username",
        "display_name",
        "email",
        "telegram_identity__username",
    )

    ordering = ("-date_joined",)

    readonly_fields = (
        "last_login",
        "date_joined",
        "updated_at",
    )

    fieldsets = DjangoUserAdmin.fieldsets + (
        (
            "MGSM information",
            {
                "fields": (
                    "display_name",
                    "updated_at",
                ),
            },
        ),
    )

    fieldsets = DjangoUserAdmin.fieldsets + (
        (
            "MGSM information",
            {
                "fields": (
                    "display_name",
                    "updated_at",
                ),
            },
        ),
    )


@admin.register(TelegramIdentity)
class TelegramIdentityAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_id",
        "username",
        "user",
        "language_code",
        "created_at",
    )

    list_filter = (
        "is_bot",
        "language_code",
        "created_at",
    )

    search_fields = (
        "=telegram_id",
        "username",
        "first_name",
        "last_name",
        "user__username",
    )

    autocomplete_fields = ("user",)

    readonly_fields = (
        "created_at",
        "updated_at",
        "raw_data",
    )

    ordering = ("-created_at",)
