from django.urls import path
from .views import SurveyList, SurveyDetail, UserSurveyList, UserRegistrationView, UserLoginView, TokenVerificationView, AnswerSurveyView, SendInvitations

urlpatterns = [
    path('surveys/', SurveyList.as_view(), name='survey-list'),
    path('surveys/<int:pk>/', SurveyDetail.as_view(), name='survey-detail'),
    path('surveys/<int:pk>/send-invitations/', SendInvitations.as_view(), name='send-invitations'),
    path('my-surveys/', UserSurveyList.as_view(), name='user-surveys'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('verify-token/<str:token>/', TokenVerificationView.as_view(), name='token-verification'),
    path('answer-survey/<int:survey_id>/<str:token>/', AnswerSurveyView.as_view(), name='answer-survey'),
]
