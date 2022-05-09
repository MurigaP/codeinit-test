from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from api.services.document import DocumentService
from api.exceptions.base import ServiceError
from rest_framework.permissions import IsAuthenticated
from api.exceptions.base import error_response
from api.serializers import DocumentSerializer
from .util import paginate_results


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DocumentSerializer

    # Retrieving uploaded documents api
    def get_queryset(self):
        return []

    # Document upload api endpoint
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

    # Retrieving user uploaded documents api
    @paginate_results
    @action(methods=["GET"], detail=False, url_path="documents", url_name="documents")
    def list_documents(self, request):
        user_id = request.user.id
        service = DocumentService(user_id=user_id)
        return self.filter_queryset(service.list_documents())
