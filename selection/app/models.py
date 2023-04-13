from django.db import models

class Item(models.Model):
    length = models.FloatField()
    Dia_dr = models.FloatField()
    T_Force = models.FloatField()
    T_Torque = models.FloatField()
    T_Weight = models.CharField(max_length=20)
    map_code = models.CharField(max_length=20)

    class Meta: 
        db_table = 'test_data'



