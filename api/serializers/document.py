from rest_framework import serializers
from api.serializers import UserSerializer
from api.models import Document
import xml.etree.ElementTree as ET
from api.exceptions.base import InvalidFileError, FileUploadError


class DocumentSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField("get_file_path")
    created_by = UserSerializer()

    class Meta:
        model = Document
        fields = [
            "id",
            "original_file_name",
            "file",
            "created_by",
            "created_at",
        ]

    def get_file_path(self, obj):
        request = self.context.get("request")
        file = obj.file.url
        # full_url = settings.DOMAIN + file
        full_url = ""
        # return request.build_absolute_uri(file)
        return full_url


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, file):
        et = ET.parse(file)
        root = et.getroot()
        allowable_tag = "iati-activities"
        if root.tag != allowable_tag:
            raise InvalidFileError()
        else:
            return file

    def create(self, validated_data):
        try:
            new_document = Document.objects.create(**validated_data)
            return new_document
        except Exception as e:
            raise FileUploadError()
