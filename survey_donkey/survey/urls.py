from django.urls import path
from .views import SurveyList, SurveyDetail, UserSurveyList, UserRegistrationView, UserLoginView, TokenVerificationView

urlpatterns = [
    path('surveys/', SurveyList.as_view(), name='survey-list'),
    path('surveys/<int:pk>/', SurveyDetail.as_view(), name='survey-detail'),
    path('my-surveys/', UserSurveyList.as_view(), name='user-surveys'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('verify-token/<str:token>/', TokenVerificationView.as_view(), name='token-verification'),
]