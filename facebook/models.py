from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from your_project import settings


# Added since "AttributeError"
# REQUIRED_FIELDS = ('user',)
# USERNAME_FIELD = 'user'

class MyCustomProfile(FacebookModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    @receiver(post_save)
    def create_profile(sender, instance, created, **kwargs):
        """Create a matching profile whenever a user object is created."""
        if sender == get_user_model():
            user = instance
            profile_model = get_profile_model()
        if profile_model == MyCustomProfile and created:
            profile, new = MyCustomProfile.objects.get_or_create(user=instance)