from django.contrib import admin

from .models import Choice, Question
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ] # This is for order the fields in Question creation.
    inlines = [ChoiceInline] # Create choices in Question page.
    list_display = ('question_text', 'pub_date', 'was_published_recently') # Info showed in question list.
    list_filter = ['pub_date'] # Add a filter to the right.
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
