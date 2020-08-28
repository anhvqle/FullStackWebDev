from django.contrib import admin
from . import models

class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'release_year', 'length']
    search_fields = ['title']
    list_filter = ['release_year','length']
    list_display = ['title','release_year','length']
    list_editable = ['length']

admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
