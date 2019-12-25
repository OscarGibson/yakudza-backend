from django.db import models
from datetime import datetime, time

class WorkHours(models.Model):

    start_hours = models.TimeField()
    end_hours = models.TimeField()
    title = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return "Години роботи"

    @property
    def opened(self):
        now = datetime.utcnow()
        current_time = time(
            hour=now.hour,
            minute=now.minute,
            second=now.second
        )
        return not (self.start_hours < current_time < self.end_hours)
