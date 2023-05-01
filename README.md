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
2. setting up base.html:
    - navbar code in store/templates/store/base.html
    - extends base.html store/templates/store/store.html
3. setting up foreign key constraint:
    - in store.models.Product: 
        - category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
4. Enabling category dropdown (in navbar) on all pages (using context_processors):
    - in store.views.py: return {'all_categories': models.Category.objects.all()}
    - in settings.py: TEMPLATES: OPTIONS: context_processors: append store.views.categories
    - in store/templates/store/base.html: <!-- we can directly loop through all_categories (key of dict returned from views.categories) without using render and context(i.e. invoking the views.categories), given that we have append it already in context_processors in settings.py -->
      {% for category in all_categories %}
        <li><a class="dropdown-item" href="">{{ category.name | capfirst }}</a></li>
      {% endfor %}