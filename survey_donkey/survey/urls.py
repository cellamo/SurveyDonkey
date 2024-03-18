# Import necessary modules
from django.urls import path
from .views import SurveyList, UserSurveyList, UserRegistrationView, UserLoginView, TokenVerificationView, AnswerSurveyView, SendInvitations
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SurveyDetailView, SurveyCreateView, SurveyDeleteView

# Define URL patterns
urlpatterns = [
    path('surveys/', SurveyList.as_view(), name='survey-list'),  # URL pattern for survey list
    path('survey/<int:survey_id>/', SurveyDetailView.as_view(), name='survey-detail'),  # URL pattern for survey detail
    path('surveys/create/', SurveyCreateView.as_view(), name='survey-create'),  # URL pattern for survey create
    path('surveys/<int:pk>/delete/', SurveyDeleteView.as_view(), name='survey-delete'),
    path('surveys/<int:pk>/send-invitations/', SendInvitations.as_view(), name='send-invitations'),  # URL pattern for sending invitations

    path('my-surveys/', UserSurveyList.as_view(), name='user-surveys'),  # URL pattern for user's surveys

    path('register/', UserRegistrationView.as_view(), name='register'),  # URL pattern for user registration
    path('login/', UserLoginView.as_view(), name='login'),  # URL pattern for user login
    path('verify-login/<str:token>/', TokenVerificationView.as_view(), name='token-verification'),  # URL pattern for token verification
    
    path('invited-survey/<int:survey_id>/<str:token>/', AnswerSurveyView.as_view(), name='answer-survey'),  # URL pattern for answering a survey


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]