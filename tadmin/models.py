from django.db import models

# Create your models here.
from rest_framework.serializers import ModelSerializer


class Routine(models.Model):
    DAY_SEL=[
        ('MONDAY','MONDAY'),
        ('TUESDAY','TUESDAY'),
        ('WEDNESDAY','WEDNESDAY'),
        ('THURSDAY','THURSDAY'),
        ('FRIDAY','FRIDAY'),
        ('SATURDAY','SATURDAY'),
        ('SUNDAY','SUNDAY'),
        ]
    
    sub=models.CharField(max_length=50)
    teacher=models.CharField(max_length=50)
    shift=models.PositiveIntegerField()
    weekday=models.CharField(choices=DAY_SEL)

    def __str__(self) :
        return str(f'{self.weekday}-{self.shift}-{self.sub}')

class RoutineSerializers(ModelSerializer):
    class Meta:
        model=Routine
        fields='__all__'