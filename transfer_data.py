import os
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shiksha.settings')
django.setup()

from tadmin.models import classes, Routine  # Import your models

def transfer_data():
    # Query data from the 'two' database
    with django.db.connections['two'].cursor() as cursor:
        # Get all data from 'classes' model
        cursor.execute("SELECT * FROM tadmin_classes")
        classes_data = cursor.fetchall()

        # Insert data into 'default' database
        for data in classes_data:
            classes.objects.using('default').create(
                id=data[0],
                class_state=data[1]
            )

        # Get all data from 'routine' model
        cursor.execute("SELECT * FROM tadmin_routine")
        routine_data = cursor.fetchall()

        # Insert data into 'default' database
        for data in routine_data:
            Routine.objects.using('default').create(
                id=data[0],
                sub=data[1],
                teacher=data[2],
                shift=data[3],
                weekday=data[4]
            )

if __name__ == '__main__':
    transfer_data()
