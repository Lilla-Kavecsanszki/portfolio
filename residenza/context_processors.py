from django.conf import settings


def available_languages(request):
    """
    Context processor to make LANGUAGES available to all templates.
    """
    return {"LANGUAGES": settings.LANGUAGES}
