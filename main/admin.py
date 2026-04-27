from django.contrib import admin
from .models import Language, TranslationHistory

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
@admin.register(TranslationHistory)
class TranslationHistoryAdmin(admin.ModelAdmin):
    list_display = ('source_text', 'translated_text', 'from_lang', 'to_lang', 'created_at')
    search_fields = ('source_text', 'translated_text')
    list_filter = ('from_lang', 'to_lang', 'created_at')
