from django.contrib.auth import get_user_model

__all__ = [get_user_model, "Document"]

from .core.document import Document
