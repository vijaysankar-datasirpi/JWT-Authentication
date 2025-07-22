from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import user_serializer
from .models import users
import jwt,datetime

class UserSignUp(APIView):
    def post(self, request):
        serializer = user_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"})
        return Response(serializer.errors)

class UserLogIn(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = users.objects.filter(email=email).first()
        if user is None:
            return Response({"error": "Invalid user"}, status=400)

        if user.password != password:
            return Response({"error": "Incorrect password"}, status=400)

        payload={
            "id":user.id,
            "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            "iat":datetime.datetime.utcnow()
        }

        response=Response()

        token=jwt.encode(payload,'secret',algorithm='HS256')
        response.set_cookie(key='jwt',value=token,httponly=True)

        return response
    
class UserPasswordView(APIView):
    def get(self,request):
        serializer=user_serializer(request.user)
        if not serializer:
            return Response({"error":"Unauthenticated"},status=403)
        return Response({"username":serializer.data['username']})
    
class UserProfileView(APIView):
    def get(self,request):
        serializer=user_serializer(request.user)
        if serializer.data['role'] != 'admin':
            return Response({"error":"Unauthenticated"},status=403)
        return Response({"Message":"Success"})