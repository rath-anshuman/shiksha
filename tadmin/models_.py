from django.db import models

from rest_framework.serializers import ModelSerializer,ListSerializer,Serializer


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

    SECTION=[
        ('A1','A1'),
        ('A2','A2'),
        ('B1','B1'),
        ('B2','B2'),
        ('C1','C1'),
        ('C2','C2'),
    ]

    sub=models.CharField(max_length=50)
    teacher=models.CharField(max_length=50)
    shift=models.IntegerField(choices=SHIFTS)
    section=models.IntegerField(choices=SECTION)
    weekday=models.CharField(choices=DAY_SEL)

    def __str__(self) :
        return str(f'{self.weekday}-{self.shift}-{self.sub}')
