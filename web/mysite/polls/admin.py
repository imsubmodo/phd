
from polls.models import Poll
from polls.models import Choice

from django.contrib import admin

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
  date_hierarchy = 'pub_date'
  search_fields = ['question']
  list_filter = ['pub_date']
  list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)
