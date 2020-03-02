from django.contrib import admin
from .models import Room, Player, Monster
# Register your models here.

admin.site.register(Monster)
admin.site.register(Room)
admin.site.register(Player)