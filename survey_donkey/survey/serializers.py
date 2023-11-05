from rest_framework import serializers
from .models import User, Survey, Question, Choice, Answer, Invitation

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
        # Replace '...' with the actual fields of the Answer model
        fields = ['...']

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        # Replace '...' with the actual fields of the Invitation model
        fields = ['...']