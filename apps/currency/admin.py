from django.contrib import admin
from .models import Portfolio, AssetsUser, Asset
# Register your models here.
admin.site.register(Portfolio)
admin.site.register(AssetsUser)
admin.site.register(Asset)