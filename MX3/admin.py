from django.contrib import admin
from django.contrib.auth.models import User
from .models import Publishert, Gamestudiot, Gametitlet, Gamert

admin.site.register(Publishert)
admin.site.register(Gamestudiot)
admin.site.register(Gametitlet)
admin.site.register(Gamert)
