import endpoints
import httplib


class MethodNotAllowed(endpoints.ServiceException):
    http_status = httplib.METHOD_NOT_ALLOWED