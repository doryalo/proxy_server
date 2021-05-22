from rest_framework import status
from rest_framework.exceptions import APIException


class MissingTaskIDError(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Task ID must be supplied'
    default_code = 'error'


class UnknownTaskIDError(APIException):
    pass