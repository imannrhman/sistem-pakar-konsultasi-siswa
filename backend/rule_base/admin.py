from django.contrib import admin
from .models import RuleBase

class RuleBaseAdmin(admin.ModelAdmin):
        list_display = ('behavior_code', 'questions_code')

# Register your models here.
admin.site.register(RuleBase, RuleBaseAdmin)