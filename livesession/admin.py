from django.contrib import admin

# Register your models here.
from .models import livesession_Links
from .models import feedback

admin.site.register(livesession_Links)
admin.site.register(feedback)