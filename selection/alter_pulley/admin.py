from django.contrib import admin
from .models import Item
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class ItemAdmin(UserAdmin):
    list_display = ('length', 'Dia_dr', 'T_Force', 'T_Weight', 'T_Weight_J', 'map_code')