import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

import random
from second_app.models import User
from faker import Faker

fakeGen = Faker()

def populate(N = 5):
    for entry in range (N):
        fake_name = fakeGen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakeGen.email()

        user = User.objects.get_or_create(first_name = fake_fname, last_name = fake_lname, email = fake_email)[0]

if __name__ == '__main__':
    print("populating databases...")
    populate(20)
    print("populating completed!")
