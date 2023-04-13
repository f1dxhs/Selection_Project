from django.contrib import admin
from .models import Item
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class ItemAdmin(UserAdmin):
    list_display = ('length', 'Dia_dr', 'T_Force', 'T_Torque', 'T_Weight', 'map_code')