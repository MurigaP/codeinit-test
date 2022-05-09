from api.serializers import UserSerializer
import logging
from api.exceptions.base import UserDoesNotExist
from django.db.models import Q


from django.contrib.auth import get_user_model

User = get_user_model()


"""
User Service to handle:
1 . Retrieve user details
2. Search user details
"""


class UserService:
    def __init__(self, user_id=None):
        self._logger = logging.getLogger("django")
        self._user_id = user_id if user_id != None else None
        self.success_response = {"message": "success"}

    def get_user_details(self, user_id=None):
        return self.__get_user_info(user_id)

    def search_user_by_username(self, data):
        try:
            return User.get(Q(email=data.get("email") or None))
        except Exception as exception:
            self._logger.error(msg=f"{exception}", exc_info=True)
            raise UserDoesNotExist() from exception

    def __get_user_info(self, user_id=None):
        if user_id is None:
            user_id = self._user_id
        try:
            return User.objects.get(Q(id=user_id))
        except Exception as exception:
            self._logger.error(msg=f"{exception}", exc_info=True)
            raise UserDoesNotExist() from exception

    def get_user_profile_info(self):
        record = self.__get_user_info()
        response = UserSerializer(record, many=False).data
        return response
