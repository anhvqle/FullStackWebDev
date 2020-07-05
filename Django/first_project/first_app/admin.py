from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord
# Register your models here.
admin.sites.register(Topic)
admin.sites.register(Webpage)
admin.sites.register(AccessRecord)
