import jwt
from .models import users
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from jwt.exceptions import ExpiredSignatureError,InvalidTokenError

class JWTMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        path=['/user/getprofile','/user/getusername']
        if request.path in path:
            token=request.COOKIES.get('jwt')
            if not token:
                raise AuthenticationFailed("Unauthenticated")
            try:
                payload=jwt.decode(token,'secret',algorithms=['HS256'])
            except ExpiredSignatureError:
                raise AuthenticationFailed("Unauthenticated")
            except InvalidTokenError:
                raise AuthenticationFailed("Invalid Token")
            user=users.objects.filter(id=payload['id']).first()
            if user == None:
                raise AuthenticationFailed("Unauthenticated")
            request.user=user
        response=self.get_response(request)
        return response