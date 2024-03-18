from django.contrib import admin
from .models import User, Survey, QuestionType, Question, Invitation, ResponseToQuestion

# Customize the User admin view
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

# Customize the Survey admin view
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'creator', 'start_time', 'end_time', 'created_at')
    list_filter = ('start_time', 'end_time', 'creator')
    search_fields = ('title', 'creator__email')

# Customize the QuestionType admin view
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Customize the Question admin view
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'question_type', 'choices', 'order', 'is_required')
    list_filter = ('survey', 'question_type', 'is_required')
    search_fields = ('question_text',)

# Customize the Invitation admin view
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'email', 'invitation_link', 'created_at', 'expiration_date')
    list_filter = ('survey', 'created_at', 'expiration_date', 'email')
    search_fields = ('email', 'invitation_link')

# Customize the Response admin view
class ResponseToQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'question', 'answer_text', 'selected_choices')
    list_filter = ('survey', 'question')
    search_fields = ('answer_text',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(QuestionType, QuestionTypeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Invitation, InvitationAdmin)
admin.site.register(ResponseToQuestion, ResponseToQuestionAdmin)

