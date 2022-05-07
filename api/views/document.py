from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from api.services.document import DocumentService
from api.exceptions.base import ServiceError
from rest_framework.permissions import IsAuthenticated
from api.exceptions.base import error_response


class DocumentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return []

    @action(
        methods=["POST"],
        detail=False,
        url_path="iatidoc",
        url_name="iatidoc",
    )
    def upload_file(self, request):
        user_id = request.user.id
        service = DocumentService(user_id=user_id)
        try:
            return Response(service.upload_file(request))
        except ServiceError as exception:
            return error_response(exception)

    @action(methods=["GET"], detail=False, url_path="details", url_name="details")
    def fetch_document_details(self, request):
        user_id = request.user.id
        payload = request.query_params.dict()
        service = DocumentService(
            user_id=user_id, document_id=payload.get("document_id", None)
        )
        try:
            return Response(service.get_document_details_info())
        except ServiceError as exception:
            return error_response(exception)
