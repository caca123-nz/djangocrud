from django.contrib import admin
from mainapp.models import Main

@admin.register(Main)
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
