from django.db import models
import uuid
import os
from datetime import datetime

from api.models.base import BaseModel

# This
def create_directory_path():
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    dir_path = str(current_year) + "/" + str(current_month)
    return dir_path


def file_upload(instance, filename):
    ext = filename.split(".")[-1]
    upload_to = create_directory_path()
    if instance.pk:
        filename = "{}.{}".format(instance.pk, ext)
    else:
        filename = "{}.{}".format(uuid.uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Document(BaseModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )
    original_file_name = models.CharField(max_length=500)
    file = models.FileField(upload_to=file_upload)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "documents"
