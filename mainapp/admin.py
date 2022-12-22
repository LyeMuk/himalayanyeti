from django.contrib import admin
from .models import categories
from .models import label
from .models import article


# Register your models here.

admin.site.register(article)
admin.site.register(label)
admin.site.register(categories)

