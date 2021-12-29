from django.contrib import admin
from .models import Behavior, Problem, Solution
from behaviors import models

# Register your models here.
class ProblemInline(admin.StackedInline):
        model = Problem

class SolutionInline(admin.StackedInline):
        model = Solution

class BehaviorAdmin(admin.ModelAdmin) :
        list_display = ('code', 'name', 'created_at')
        inlines = [ProblemInline, SolutionInline]


class ProblemAdmin(admin.ModelAdmin) :
        list_display = ('code', 'problem', 'text') 

class SolutionAdmin(admin.ModelAdmin):
        list_display = ('code', 'problem', 'text')


admin.site.register(Behavior, BehaviorAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)