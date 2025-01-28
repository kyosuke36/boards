from django.contrib import admin

from .models import Money
from .models import Result

admin.site.register(Money)
admin.site.register(Result)
