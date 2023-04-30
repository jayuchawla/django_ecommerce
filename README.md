### E commerce using Django

#### Learnings
1. in store:
    - create a directory: templates/store
    - create a file: templates/store/store.html
    - create a file: urls.py
        -   urlpatterns = [path('', views.store, name='store')]
    - in root urls.py: append in urlpatterns
        - path('', include('store.urls')) # store app is already defined in settings 
    - in store.views:
        - def store(request): return render(request, 'store/store.html')