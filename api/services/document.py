import logging
from api.serializers import UploadFileSerializer
from api.serializers import DocumentSerializer
from api.exceptions.base import SerializerError
from api.exceptions.base import FileDoesNotExistError
from api.exceptions.base import NoFilesforUploadError
from api.services.user import UserService
from api.models.core.document import Document
import xml.etree.ElementTree as ET


class DocumentService:
    def __init__(self, user_id=None, document_id=None, documents=[]):
        self._logger = logging.getLogger("django")
        self._user_id = user_id if user_id != None else None
        self.success_response = {"message": "success"}
        self.document_id = document_id if document_id != None else None
        self.documents = documents

    def upload_file(self, request):
        payload = request.data
        if not payload:
            raise NoFilesforUploadError()
        user_service = UserService(user_id=self._user_id)
        user_record = user_service.get_user_details()
        serializer = UploadFileSerializer(data=payload, many=False)
        if not serializer.is_valid():
            raise SerializerError(serializer.errors)
        document_obj = serializer.save()
        response = {"message": "success", "document_id": document_obj.id}
        return response

    def __get_document_info(self, document_id=None):
        if document_id is None:
            document_id = self.document_id
        try:
            return Document.objects.get(Q(id=document_id))
        except Exception as exception:
            self._logger.error(msg=f"{exception}", exc_info=True)
            raise FileDoesNotExistError() from exception

    def get_document_details_info(self):
        record = self.__get_document_info()
        response = DocumentSerializer(record, many=False).data
        return response
