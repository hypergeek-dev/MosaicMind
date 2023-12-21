import os
import django
import sys
sys.path.append('C:/Projects/MosaicMind') 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mosaicminds.settings')
django.setup()
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
import uuid
from eventmanager.models import Profile 
User = get_user_model()

users_data = [
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Emily",
        "last_name": "Taylor",
        "email": "emily.taylor01@example.com",
        "phone_number": "+44 7700 900001",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Oliver",
        "last_name": "Johnson",
        "email": "oliver.johnson02@example.com",
        "phone_number": "+44 7700 900002",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Ava",
        "last_name": "Brown",
        "email": "ava.brown03@example.com",
        "phone_number": "+44 7700 900003",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Liam",
        "last_name": "Davis",
        "email": "liam.davis04@example.com",
        "phone_number": "+44 7700 900004",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Sophia",
        "last_name": "Wilson",
        "email": "sophia.wilson05@example.com",
        "phone_number": "+44 7700 900005",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "James",
        "last_name": "Moore",
        "email": "james.moore06@example.com",
        "phone_number": "+44 7700 900006",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Isabella",
        "last_name": "Martin",
        "email": "isabella.martin07@example.com",
        "phone_number": "+44 7700 900007",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Ethan",
        "last_name": "Jackson",
        "email": "ethan.jackson08@example.com",
        "phone_number": "+44 7700 900008",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Mia",
        "last_name": "Thompson",
        "email": "mia.thompson09@example.com",
        "phone_number": "+44 7700 900009",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Noah",
        "last_name": "White",
        "email": "noah.white10@example.com",
        "phone_number": "+44 7700 900010",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Amelia",
        "last_name": "Harris",
        "email": "amelia.harris11@example.com",
        "phone_number": "+44 7700 900011",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Harry",
        "last_name": "Young",
        "email": "harry.young12@example.com",
        "phone_number": "+44 7700 900012",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Charlotte",
        "last_name": "King",
        "email": "charlotte.king13@example.com",
        "phone_number": "+44 7700 900013",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "William",
        "last_name": "Wright",
        "email": "william.wright14@example.com",
        "phone_number": "+44 7700 900014",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Ella",
        "last_name": "Mitchell",
        "email": "ella.mitchell15@example.com",
        "phone_number": "+44 7700 900015",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Benjamin",
        "last_name": "Carter",
        "email": "benjamin.carter16@example.com",
        "phone_number": "+44 7700 900016",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Lucy",
        "last_name": "Phillips",
        "email": "lucy.phillips17@example.com",
        "phone_number": "+44 7700 900017",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Henry",
        "last_name": "Walker",
        "email": "henry.walker18@example.com",
        "phone_number": "+44 7700 900018",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Grace",
        "last_name": "Robinson",
        "email": "grace.robinson19@example.com",
        "phone_number": "+44 7700 900019",
    },
    {
        "username": str(uuid.uuid4()),
        "password": get_random_string(12),
        "first_name": "Logan",
        "last_name": "Lee",
        "email": "logan.lee20@example.com",
        "phone_number": "+44 7700 900020",
    },
]
for user_data in users_data:
    user = User.objects.create_user(
        username=user_data["username"],
        password=get_random_string(12),
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        email=user_data["email"],
    )

    Profile.objects.create(
        user=user,
        phone_number=user_data["phone_number"]
    )

    user.save()