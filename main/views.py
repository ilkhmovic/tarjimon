from django.shortcuts import render 
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Language, TranslationHistory
import json
from deep_translator import GoogleTranslator

def tarjimon(request):
    """Tarjimon sahifasini ko'rsatish"""
    languages = Language.objects.all()
    context = {
        'languages': languages,
    }
    return render(request, 'tarjimon.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def translate_api(request):
    """Tarjima API - simple implementation"""
    try:
        data = json.loads(request.body)
        from_lang = data.get('from_lang')
        to_lang = data.get('to_lang')
        source_text = data.get('source_text', '').strip()

        if not source_text:
            return JsonResponse({'error': 'Matn bo\'sh'}, status=400)

        if not from_lang or not to_lang:
            return JsonResponse({'error': 'Tillar tanlang'}, status=400)
        
        # Simple placeholder translation logic
        # Replace this with actual API call to translation service
        translated_text = translate_text(source_text, from_lang, to_lang)
        
        # Save to history
        try:
            from_lang_obj = Language.objects.get(code=from_lang)
            to_lang_obj = Language.objects.get(code=to_lang)
            TranslationHistory.objects.create(
                source_text=source_text,
                translated_text=translated_text,
                from_lang=from_lang_obj,
                to_lang=to_lang_obj
            )
        except Language.DoesNotExist:
            pass
        
        return JsonResponse({
            'translated_text': translated_text,
            'from_lang': from_lang,
            'to_lang': to_lang
        })
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Xato so\'rov'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def translate_text(source_text, from_lang, to_lang):
    """Actual translation function using GoogleTranslator"""
    try:
        translator = GoogleTranslator(source=from_lang, target=to_lang)
        return translator.translate(source_text)
    except Exception as e:
        return f"Tarjima xatosi: {str(e)}"

def translation_history(request):
    """Tarjima tarixini ko'rsatish"""
    history = TranslationHistory.objects.all()[:50]
    context = {
        'history': history,
    }
    return render(request, 'history.html', context)

