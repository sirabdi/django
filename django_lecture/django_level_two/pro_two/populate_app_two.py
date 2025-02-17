import os  
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro_two.settings')

import django
django.setup()

# FAKE POP SCRIPT
from app_two.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for _ in range(N):
        # Create fake data for that entry
        fake_name = fakegen.name()
        fake_email = fakegen.email()
        fake_last_name = fakegen.name()

        # Create the new user entry
        User.objects.get_or_create(first_name=fake_name,last_name=fake_last_name,email=fake_email)[0]
        

if __name__ == '__main__':
    print("populating script . . . .")
    populate(20)
    print("populating completed!")