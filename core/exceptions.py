from rest_framework.exceptions import APIException


class PageNotFound(APIException):
    status_code = 404
    default_detail = "Requested page does not exist"
    default_code = "page_not_found"
