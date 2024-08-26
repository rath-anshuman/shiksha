from django.db import models

# Create your models here.
from rest_framework.serializers import ModelSerializer,ListSerializer,Serializer


class classes(models.Model):
    active=models.BooleanField(default=True)
    def __str__(self) :
        return str(self.active)

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
    SHIFTS=[
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
            ]
    sub=models.CharField(max_length=50)
    teacher=models.CharField(max_length=50)
    shift=models.IntegerField(choices=SHIFTS)
    weekday=models.CharField(choices=DAY_SEL)

    def __str__(self) :
        return str(f'{self.weekday}-{self.shift}-{self.sub}')

class RoutineSerializers(ModelSerializer):
    class Meta:
        model=Routine
        fields='__all__'
        
class classesSerializers(ModelSerializer):
    class Meta:
        model=classes
        fields='__all__'

