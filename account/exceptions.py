from rest_framework.exceptions import APIException

class UserAlreadyRegistered(APIException):
    status_code = 400
    default_detail = "User Already Registered"
    default_code = "user_already_registered"
