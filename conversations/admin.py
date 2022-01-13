from django.contrib import admin
from . import models

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    '''Conversation Admin Definition'''
    pass
