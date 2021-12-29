from django.contrib import admin
from .models import Answer, Question

class AnswerInline(admin.TabularInline) :
        model = Answer

class QuestionAdmin(admin.ModelAdmin):
        list_display = ('code', 'text', 'created_at')
        inlines = [AnswerInline]

# Register your models here.
admin.site.register(Question, QuestionAdmin)