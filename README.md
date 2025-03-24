# CryptoPayBackend


##  Registration
1) http://192.168.5.97:8000/api/v1/auth/users/

{
    "email" : "grigoryan021201@gmail.com",
    "terms_accepted" : true
}


# Verify Code
2) http://192.168.5.97:8000/api/v1/auth/verify-code/
{
    "email" : "grigoryan021201@gmail.com",
    "code" : 533712,
    "purpose" : "email_verification"
}

# Public Set Password
3) http://192.168.5.97:8000/api/v1/auth/public-set-password/
{
    "email": "grigoryan021201@gmail.com",
    "password": "Gago123@",
    "repeat_password": "Gago123@"
}



##  Auth
# Get JWT Token
1) http://192.168.5.97:8000/api/v1/auth/token/obtain/
{
    "email" : "grigoryan021201@gmail.com",
    "password" : "Gago123@"
}


# Verify Token
2) http://192.168.5.97:8000/api/v1/auth/token/verify/
{
    "token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyODUxMzYyLCJpYXQiOjE3NDI4NDgzNjIsImp0aSI6ImNhYzM3NTQ2NWYyYjQzNTZhYmEyN2VjNTJjODVlMWE2IiwidXNlcl9pZCI6Mn0.XKxJ9JXUiFDc_twllkESrDxjWLphv7KzH4ikaHcAlOE"
}


# Update Access Token
3) http://192.168.5.97:8000/api/v1/auth/token/refresh/
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MjkzNDc2MiwiaWF0IjoxNzQyODQ4MzYyLCJqdGkiOiIwOWZiNDgyMDFlMTU0NWNkYTViMWE3YzVmMWM3ODc0NyIsInVzZXJfaWQiOjJ9.e53YBwpOhSi4-tBZlMnYiIClz1gIO__3sbFidntzmjI"
}

## Account Recovery

# Send Code To Email
1) http://192.168.5.97:8000/api/v1/auth/recovery-request/
{
    "email" : "grigoryan021201@gmail.com"
}


# Verify Code
2) http://192.168.5.97:8000/api/v1/auth/verify-code/
{
    "email" : "grigoryan021201@gmail.com",
    "code" : 461707,
    "purpose" : "password_recovery"
}


# Reset Password
3) http://192.168.5.97:8000/api/v1/auth/recovery-reset-password/
{
    "email" : "grigoryan021201@gmail.com",
    "code" : 461707,
    "password" : "Gago123@@",
    "password2" : "Gago123@@"
}

# Pin Reset 
*Pin can be reseted if and only if in headers or somewhere are auth credential(acces_token)*
4) http://192.168.5.97:8000/api/v1/auth/reset-pin-request/



# Pin Reset Verify
*Pin can be verified if and only if in headers or somewhere are auth credential(acces_token)*
http://192.168.5.97:8000/api/v1/auth/reset-pin-verify/
{
    "code" : 180802
}


# RESET EMAIL


# Djoser Needed Endpoints (for Backend Devs)
1) users/ (GET, POST)
2) users/<id>/  (GET, POST, PUT, PATCH, DELETE) *Optional
3) users/me/  (GET, POST, PUT, PATCH, DELETE)

4) users/set_password/ (POST)
*Pin can be verified if and only if in headers or somewhere are auth credential(acces_token)*




