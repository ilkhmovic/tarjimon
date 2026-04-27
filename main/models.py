from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name="Til nomi")
    code = models.CharField(max_length=10, unique=True, verbose_name="Til kodi (ISO)")

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class TranslationHistory(models.Model):
    
    source_text = models.TextField(verbose_name="Asl matn")
    translated_text = models.TextField(verbose_name="Tarjima qilingan matn")
    
    from_lang = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='from_translations')
    to_lang = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='to_translations')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Tarjima tarixi"
    
    def __str__(self):
        return f"{self.from_lang.code} → {self.to_lang.code}: {self.source_text[:50]}"

