import os
import django
import random
import datetime
import uuid
import sys
sys.path.append('C:/Projects/MosaicMind') 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mosaicminds.settings')
django.setup()
from django.contrib.auth import get_user_model
from eventmanager.models import Meeting

User = get_user_model()

# Meeting names
meeting_names = [
    "NeuroConnect Hub", "DiverseMinds Forum", "InclusiveBrain Lounge",
    "NeuroHarmony Circle", "NeuroLife Oasis", "MindfulNeuro Nexus",
    "NeuroUnity Space", "NeuroThrive Haven", "SpectrumSoul Studio",
    "NeuroWave Assembly", "BeyondLabels Chamber", "EmbraceNeuro Network",
    "NeuroQuest Guild", "EmpowerMind Collective", "NeuroVoyage Oasis",
    "MindfulDiversity Den", "NeuroNurture Plaza", "NeuroSpectrum Junction",
    "NeuroGrowth Oasis", "EnlightenMinds Pavilion"
]

# Fetch all users
users = User.objects.all()

# Create a meeting for each user (up to 20 users)
for user, name in zip(users, meeting_names):
    meeting = Meeting.objects.create(
        name=name,
        meeting_time=datetime.time(random.randint(8, 18), random.choice([0, 30])),
        area=random.choice([choice[0] for choice in Meeting.AREA_CHOICES]),
        description="Generated meeting description.",
        online_meeting_url="http://example.com/meeting/" + str(uuid.uuid4()),
        added_by=user
    )
