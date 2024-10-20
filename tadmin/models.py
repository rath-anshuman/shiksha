from django.db import models
from rest_framework.serializers import ModelSerializer,ListSerializer,Serializer

class classes(models.Model):
    CLSST=[
        ('CLASSDAY','CLASSDAY'),
        ('HOLIDAY','HOLIDAY'),
        ('EXAMS','EXAMS'),
        ]
    class_state =models.CharField(choices=CLSST)
    
    def __str__(self) :
        return str(self.class_state)

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
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
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
    # s_time=models.TimeField(default="6:0:0")
    # e_time=models.TimeField(default="7:0:0")
    shift=models.IntegerField(choices=SHIFTS)
    section=models.CharField(choices=SECTION)
    weekday=models.CharField(choices=DAY_SEL)

    def __str__(self) :
        return str(f'{self.section}-{self.weekday}-{self.shift}-{self.sub}')

class RoutineSerializers(ModelSerializer):
    class Meta:
        model=Routine
        fields='__all__'
        
class classesSerializers(ModelSerializer):
    class Meta:
        model=classes
        fields=['class_state']    
