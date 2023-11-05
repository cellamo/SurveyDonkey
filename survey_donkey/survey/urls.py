from django.urls import path
from .views import SurveyList, SurveyDetail, UserSurveyList

urlpatterns = [
    path('surveys/', SurveyList.as_view(), name='survey-list'),
    path('surveys/<int:pk>/', SurveyDetail.as_view(), name='survey-detail'),
    path('my-surveys/', UserSurveyList.as_view(), name='user-surveys'),
]