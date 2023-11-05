from django.contrib import admin
from .models import User, Survey, Question, Choice, Answer, Invitation

# Customize the User admin view
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Customize the Survey admin view
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'start_time', 'end_time')
    list_filter = ('start_time', 'end_time')
    search_fields = ('title', 'creator__email')

# Customize the Question admin view
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'question_type')
    list_filter = ('survey', 'question_type')
    search_fields = ('text',)

# Customize the Choice admin view
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'text')
    list_filter = ('question',)
    search_fields = ('text',)

# Customize the Answer admin view
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'text', 'selected_choice')
    list_filter = ('question',)
    search_fields = ('text', 'selected_choice__text')

# Customize the Invitation admin view
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'email', 'code', 'expiration_date', 'sent_date')
    list_filter = ('survey', 'sent_date')
    search_fields = ('email', 'code')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Invitation, InvitationAdmin)
