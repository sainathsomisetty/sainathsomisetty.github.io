from django.contrib import admin
from .models import Question, Choice


class choiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questions', {'fields': ['question_text']}),
        ('publication date', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [choiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)

