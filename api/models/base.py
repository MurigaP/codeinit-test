from django.conf import settings
from django.db import models
from django.utils import timezone
from crum import get_current_user


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class BaseModel(models.Model):

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = AutoDateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_createdby",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_modifiedby",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
        default_permissions = ()

    def save(self, *args, **kwargs):  # pylint: disable=signature-differs
        """
        This automatically sets the created_by and updated_by fields based on the logged in user
        for any change to the BaseModel.
        """
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.created_by and not self.pk:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)
