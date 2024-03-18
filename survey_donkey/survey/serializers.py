from rest_framework import generics, serializers
from .models import User, Survey, Question, QuestionType, Invitation, ResponseToQuestion
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'login_token', 'login_token_expiration']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'choices', 'order', 'is_required']

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Survey
        fields = ['id', 'title', 'description','questions', 'creator', 'start_time', 'end_time', 'created_at']

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'name']


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['id', 'survey', 'email', 'invitation_link', 'created_at', 'expiration_date']

class ResponseToQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseToQuestion
        fields = ['id', 'survey', 'question', 'invitation', 'answer_text', 'selected_choices']

class SurveyDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Survey
        fields = ['id', 'title', 'description', 'start_time', 'end_time', 'created_at', 'questions']
        read_only_fields = ['creator']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        survey = Survey.objects.create(**validated_data)
        for question_data in questions_data:
            question_data['survey'] = survey
            Question.objects.create(**question_data)
        return survey
