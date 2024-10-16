from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from properties.sitemap import PropertySitemap

from residenza127.views import handler404 as custom_handler404

from .views import language_switch

# Custom 404 error handler
handler404 = "residenza127.views.handler404"

sitemaps = {
    'properties': PropertySitemap,
}

# Define the URL patterns for the app
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("properties/", include("properties.urls")),
    path("construction/", include("construction.urls")),
    path("profiles/", include("profiles.urls")),
    path("contact/", include("contact.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('residenza.urls')),
]

# Add language switching URL pattern outside i18n_patterns
urlpatterns += [
    path("language/<str:lang_code>/", language_switch, name="language_switch"),
    
]

# Adding i18n_patterns to handle language prefixes
urlpatterns += i18n_patterns(
    path("accounts/", include("allauth.urls")),
    path("properties/", include("properties.urls")),
    path("construction/", include("construction.urls")),
    path("profiles/", include("profiles.urls")),
    path("contact/", include("contact.urls")),
    path('', include('residenza.urls')),
    prefix_default_language=True,
)

# Serve static files (only in development; for production use a web server)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
