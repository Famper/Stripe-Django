from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_display_links = ('name',)
    list_per_page = 20
    list_editable = ('price',)

    fieldsets = [
        ('Основная информация', {'fields': ['name', 'price', 'description']})
    ]


admin.site.register(Item, ItemAdmin)
