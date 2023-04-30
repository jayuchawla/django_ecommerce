### E commerce using Django

#### Learnings
-   Setting up serving static content (includes media) 
    -   in settings.py:
        -   Base url to serve static files
            STATIC_URL = '/static/'

        -   Path where static files are stored
            STATICFILES_DIR = os.path.join(BASE_DIR, 'static')

        -   Base url to serve media files
            MEDIA_URL = '/media/'

        -   Path where media is stored
            MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
    -   in urls.py:
        from django.conf import settings
        from django.conf.urls.static import static
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)