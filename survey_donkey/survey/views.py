from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import Survey, User
from .serializers import SurveySerializer

User = get_user_model()
    
    
class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated]


class UserSurveyList(generics.ListAPIView):
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Survey.objects.filter(creator=user)

class UserRegistrationView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(email=email)
        token = User.objects.create_login_token(email)  # Generate the login token

        # Construct the verification URL
        verification_url = f"http://frontend-url.com/verify/{token}"  
        
        message = Mail(
        from_email='surveydonkey@arslan.wtf',
        to_emails=email,)
            
        message.dynamic_template_data = {
            'verification_url': verification_url
        }

        message.template_id = "d-7df7ce653b9e4785b3b7e64a15d3ea34"
        
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))

        
        return Response({"message": "Registration email sent. Check your inbox."}, status=status.HTTP_200_OK)
    
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            token = User.objects.create_login_token(email)

            login_url = f"http://frontend-url.com/login/{token}"  # Replace with frontend URL

            message = Mail(
            from_email='surveydonkey@arslan.wtf',
            to_emails=email,)
            
            message.dynamic_template_data = {
                'login_url': login_url
            }

            message.template_id = "d-9bb7bf40306543b49a7a397ae73eaaa5"
        
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(str(e))

            return Response({"message": "Login email sent. Check your inbox."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

class TokenVerificationView(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(login_token=token, login_token_expiration__gt=get_current_time())
            # Token is valid, so perform the required action (register or log in the user)
            # You can create a session or a JWT token here for the user

            # Optionally, clear the token after use
            user.login_token = None
            user.login_token_expiration = None
            user.save()

            return Response({"message": "Token verified successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
        
def get_current_time():
    return timezone.now()