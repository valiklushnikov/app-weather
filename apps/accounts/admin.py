from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("email", "password", "username")}),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
    )
    list_display = (
        "id",
        "email",
        "last_login",
        "date_joined",
    )

    list_display_links = ("email",)
    list_filter = (
        "is_staff",
        "is_superuser",
    )
    search_fields = ("email", "username")
    ordering = ("-email", "-date_joined")
    readonly_fields = ("last_login", "date_joined")
