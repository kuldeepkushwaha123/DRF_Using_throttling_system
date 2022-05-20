from .serializers import SignupSerializer,LoginSerializer,MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .throttling import UserThrottle

# Create your views here.

@api_view(["POST"])
def Signup(request):
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data["password"])
            user.save()
            return Response({"success":"Account has been created!."})
        else:
            return Response(serializer.errors)


@api_view(["POST"])
def Login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        username = serializer.data.get("username")
        password = serializer.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"username": str(user), "token": str(token)})
        else:
            return Response({"error": "Invalid user credientials..!"})





class SendMessageView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserThrottle]


    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



