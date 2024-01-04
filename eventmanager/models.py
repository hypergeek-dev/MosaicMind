from django.db import models
import uuid
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.user.username

class Meeting(models.Model):
    meeting_id = models.CharField(
        max_length=100, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100, default="Mosaic Minds Meeting")
    meeting_time = models.TimeField(default=datetime.time(12, 0))
    approved = models.BooleanField(default=False)

    WEEKDAY = (
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    )

    AREA_CHOICES = (
        ('CI', 'Channel Islands Area'),
        ('CTV', 'Chiltern & Thames Valley Area'),
        ('CA', 'Cornwall Area'),
        ('DA', 'Devon Area'),
        ('DO', 'Dorset Area'),
        ('EMA', 'East Midlands Area'),
        ('ES', 'Essex Area'),
        ('FC', 'Free Counties Area'),
        ('GM', 'Greater Manchester Area'),
        ('HA', 'Hampshire Area'),
        ('KE', 'Kent Area'),
        ('L-EC', 'Lancashire - East & Central Area'),
        ('L-NE', 'London - North East Area'),
        ('L-NW', 'London - North West Area'),
        ('L-SE', 'London - South East Area'),
        ('L-SW', 'London - South West Area'),
        ('MEA', 'Merseyside Area'),
        ('NS', 'Norfolk & Suffolk Area'),
        ('NEE', 'North East England Area'),
        ('NW', 'NW England & N Wales Area'),
        ('S-EC', 'Scotland - East Coast Area'),
        ('S-EL', 'Scotland - Edinburgh & Lothians Area'),
        ('S-GW', 'Scotland - Glasgow & West Coast Area'),
        ('S-WL', 'Scotland - West Lothian Area'),
        ('SWA', 'South Wales Area'),
        ('SU', 'Surrey Area'),
        ('SX', 'Sussex Area'),
        ('HIG', 'The Highlands & Islands Groups'),
        ('TS', 'The Shires Area'),
        ('UK-FAR', 'UK Farsi Groups Area'),
        ('WC', 'West Country Area'),
        ('WM', 'West Midlands Area'),
        ('WY', 'West Yorkshire'),
        ('YH', 'Yorkshire & Humberside Area'),
   )
    area = models.CharField(max_length=20, choices=AREA_CHOICES, default='CI')
    description = models.TextField(default="Standard meeting description.")
    online_meeting_url = models.URLField(default="http://www.example.com")
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meetings'
    )

    class Meta:
        permissions = (
            ("can_approve_meeting", "Can approve meetings"),
            ("can_create_meeting", "Can create meetings"),
        )

    def __str__(self):
        return self.name