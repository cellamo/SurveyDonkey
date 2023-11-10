from rest_framework import serializers
from .models import User, Survey, Question, Choice, Answer, Invitation
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title', 'description', 'creator', 'start_time', 'end_time']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'survey', 'text', 'question_type']
        
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'text', 'selected_choice']

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['id', 'survey', 'email', 'code', 'expiration_date', 'sent_date']
        
