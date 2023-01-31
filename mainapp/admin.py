from django.contrib import admin
from .models import categories
from .models import label
from .models import article, subscriber

# adding date in admin.py
class articleAdmin(admin.ModelAdmin):
    readonly_fields = ('bid','postdate', )

# Register your models here.

admin.site.register(article,articleAdmin)
admin.site.register(label)
admin.site.register(categories)
admin.site.register(subscriber)


