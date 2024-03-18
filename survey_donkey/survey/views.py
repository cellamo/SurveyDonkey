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
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Survey, User, Question, ResponseToQuestion, Invitation
from .serializers import SurveyDetailSerializer, SurveySerializer

User = get_user_model()
    
    
class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


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
        verification_url = f"http://localhost:8000/api/verify-login/{token}/"  # Replace with the desired URL
        
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

        
        return Response({"message": "Registration email sent. Check your inbox."}, status.HTTP_200_OK)
    
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            token = User.objects.create_login_token(email)

            login_url = f"http://localhost:8000/api/verify-login/{token}/"  # Replace with the desired URL

            print(f"Preparing to send login email to: {email}")
            message = Mail(
            from_email='surveydonkey@arslan.wtf',
            to_emails=email,)
            
            message.dynamic_template_data = {
                'login_url': login_url
            }

            message.template_id = "d-9bb7bf40306543b49a7a397ae73eaaa5"
        
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                print("Sending login email via SendGrid...")
                response = sg.send(message)
                print(f"SendGrid response status code: {response.status_code}")
                print(f"SendGrid response body: {response.body}")
                print(f"SendGrid response headers: {response.headers}")
            except Exception as e:
                print(f"Error occurred while sending login email: {str(e)}")

            return Response({"message": "Login email sent. Check your inbox."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

class TokenVerificationView(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(login_token=token, login_token_expiration__gt=get_current_time())
            # Token is valid, so perform the required action (register or log in the user)

            # Optionally, clear the token after use
            user.login_token = None
            user.login_token_expiration = None
            user.save()

            # Generate JWT token
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Token verified successfully"
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
        
def get_current_time():
    return timezone.now()

class AnswerSurveyView(APIView):
    def get(self, request, survey_id, token):
        try:
            # Check if the invitation is valid
            invitation = get_object_or_404(Invitation, token=token, survey_id=survey_id)
            
            if invitation.expiration_date < get_current_time():
                return Response({"error": "Invitation expired"}, status=status.HTTP_400_BAD_REQUEST)
            
            # get the survey
            survey = get_object_or_404(Survey, id=survey_id)
            
            survey_data = SurveySerializer(survey).data
            
            invitation.delete()
            
            return Response(survey_data, status=status.HTTP_200_OK)
        except Survey.DoesNotExist:
            return Response({"error": "Survey does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Invitation.DoesNotExist:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class SendInvitations(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        try:
            survey = Survey.objects.get(id=pk, creator=request.user)
        except Survey.DoesNotExist:
            return Response({"error": "Survey does not exist or you are not the owner."}, status=status.HTTP_404_NOT_FOUND)
        
        emails = request.data.get('emails', [])
        if not emails or not isinstance(emails, list):
            return Response({"error": "Please provide a list of emails"}, status=status.HTTP_400_BAD_REQUEST)
        
        for email in emails:
            # Create an invitation for each email
            invitation = Invitation.objects.create(survey=survey, email=email)
            
            # Construct the invitation URL
            invitation_url = f"http://frontend-url.com/answer-survey/{survey.id}/{invitation.invitation_link}"
            message = Mail(
            from_email='surveydonkey@arslan.wtf',
            to_emails=email,)

            message.dynamic_template_data = {
                'invitation_url': invitation_url
            }
            
            message.template_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(str(e))
                
        return Response({"message": "Invitations sent"}, status=status.HTTP_200_OK)
            
    
class SurveyDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer

    def get_object(self):
        survey_id = self.kwargs['survey_id']
        return get_object_or_404(Survey, id=survey_id)
    
class SurveyCreateView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class SurveyDeleteView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer

    def get_object(self):
        survey_id = self.kwargs['pk']
        return get_object_or_404(Survey, id=survey_id)
    
    def destroy(self, request, *args, **kwargs):
        survey = self.get_object()
        if survey.creator != request.user:
            return Response({"error": "You are not the owner of this survey"}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(survey)
        return Response(status=status.HTTP_204_NO_CONTENT)