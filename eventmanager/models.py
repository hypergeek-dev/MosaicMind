from django.db import models
import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name# your fields here
from django.db import models
from django.conf import settings
import uuid

class Meeting(models.Model):
    meeting_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    description = models.TextField()
    online_meeting_url = models.URLField()

    # ForeignKey relationship to the User model
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meetings'
    )


    def __str__(self):
        return self.name
