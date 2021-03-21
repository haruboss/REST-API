from django.contrib import admin
from .models import *

admin.site.register([Language, Paradigms, Programmer])
