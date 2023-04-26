from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Roller_TableData(models.Model):
    Belt_Width = models.FloatField(max_length=50)
    Dia = models.FloatField(max_length=50)
    # Length = models.CharField(max_length=50)
    T_Weight = models.CharField(max_length=20)
    mapcode_2 = models.CharField(max_length=20)


    # def __str__(self):
    #     return f"{self.table.name}: {self.Belt_Width}, {self.Dia}, {self.Length}, {self.T_Weight}, {self.mapcode_2}"
    # class Meta: 
    #     db_table = 'roller_35dt_cleaned'