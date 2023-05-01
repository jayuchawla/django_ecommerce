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
5. Dynamic url routing:
    - in views.category_list:
        category_object = get_object_or_404(models.Category, slug=category_slug)
        return render(request, 'store/category_list.html', {
            'category': category_object,
            'products': models.Product.objects.filter(category=category_object)
        })
    - reverse function:
        - resolves url from name:
            - path('search/<slug:category_slug>', views.category_list, name='category_list')
        - used within get_absolute_url method in model class definition
            - return reverse('category_list', args=[self.slug])
    - in template:
        {{ category.get_absolute_url }}

###### NOTE: We could have easily used this for dynamic url routing: _<a class="stretched-link" href="{% url 'category_list' category.slug %}"></a>_
###### But the above violates the DRY (Don't Repeat Yourself) principle and the whole idea of editing in one place only - which is something to strive for - we would then be required to make change in each template if the url pattern is changed in future 