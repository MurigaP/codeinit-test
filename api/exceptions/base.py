from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


def error_response(exception, status=HTTP_400_BAD_REQUEST):
    return Response({"error": type(exception).__name__}, status=status)


# Generic Exceptions for all api related errors
class BaseError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ServiceError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidPayloadError(ServiceError):
    def __init__(self, msg=""):
        message = "Error - Invalid payload"
        if msg:
            message = msg
        super().__init__(message)


class UserDoesNotExist(ServiceError):
    def __init__(self, msg=""):
        message = "Error - User does not exist"
        if msg:
            message = msg
        super().__init__(message)


class PermissionDeniedError(ServiceError):
    def __init__(self, msg=""):
        message = "You are not allowed to perform this action"
        if msg:
            message = msg
        super().__init__(message)


class FileUploadError(ServiceError):
    def __init__(self, msg=""):
        message = "Error - An error ocurred while uploading the file"
        if msg:
            message = msg
        super().__init__(message)


class InvalidFileError(ServiceError):
    def __init__(self, msg=""):
        message = "Error - File uploaded is invalid"
        if msg:
            message = msg
        super().__init__(message)


class NoFilesforUploadError(ServiceError):
    def __init__(self, msg=""):
        message = "Error - No file to upload"
        if msg:
            message = msg
        super().__init__(message)


class FileDoesNotExistError(ServiceError):
    def __init__(self, msg=""):
        message = "Error - No file found matching criteria"
        if msg:
            message = msg
        super().__init__(message)


def _get_error_details(data, default_code=None):
    """
    Descend into a nested data structure, forcing any
    lazy translation strings or strings into `ErrorDetail`.
    """
    if isinstance(data, (list, tuple)):
        ret = [_get_error_details(item, default_code) for item in data]
        if isinstance(data, ReturnList):
            return ReturnList(ret, serializer=data.serializer)
        return ret
    elif isinstance(data, dict):
        ret = {
            key: _get_error_details(value, default_code) for key, value in data.items()
        }
        if isinstance(data, ReturnDict):
            return ReturnDict(ret, serializer=data.serializer)
        return ret

    text = force_str(data)
    code = getattr(data, "code", default_code)
    return ErrorDetail(text, code)


class SerializerError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Invalid input.")
    default_code = "invalid"

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        # For validation failures, we may collect many errors together,
        # so the details should always be coerced to a list if not already.
        if isinstance(detail, tuple):
            detail = list(detail)
        elif not isinstance(detail, dict) and not isinstance(detail, list):
            detail = [detail]

        self.detail = _get_error_details(detail, code)


class ErrorDetail(str):
    """
    Formatting errors to single response errors
    """

    code = None

    def __new__(cls, string, code=None):
        self = super().__new__(cls, string)
        self.code = code
        return self

    def __eq__(self, other):
        r = super().__eq__(other)
        if r is NotImplemented:
            return NotImplemented
        try:
            return r and self.code == other.code
        except AttributeError:
            return r

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "ErrorDetail(string=%r, code=%r)" % (
            str(self),
            self.code,
        )

    def __hash__(self):
        return hash(str(self))
