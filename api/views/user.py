from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from api.services.user import UserService
from api.exceptions.base import ServiceError
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        query_params = self.request.query_params.dict()
        page_size = query_params.get("page_size", None)
        page = query_params.get("page", None)
        if page_size:
            query_params.pop("page_size")
        if page:
            query_params.pop("page")
        service = UserService()
        return service.get_all_users(query_params)

    @action(methods=["GET"], detail=False, url_path="details", url_name="details")
    def fetch_user_details(self, request):
        payload = request.query_params.dict()
        user_id = payload.get("user_id", request.user.id)
        service = UserService(user_id=user_id)
        try:
            return Response(service.get_user_profile_info())
        except ServiceError as exception:
            from api.exceptions.base import error_response

            return error_response(exception)
