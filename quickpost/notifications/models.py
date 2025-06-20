from django.db import models
from users.models import CustomUser
from django.utils import timezone

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)  # Timestamp for when read

    def __str__(self):
        return f"Notification for {self.recipient.username} - {self.message[:20]}"

    def mark_as_read(self):
        self.is_read = True
        self.read_at = timezone.now()  # Set current time
        self.save()
