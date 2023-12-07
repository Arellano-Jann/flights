import uuid
import datetime

from django.contrib.auth.models import User, Group
from django.db import models
from django.urls import reverse
from django.conf import settings


class Flight(models.Model):
    name = models.CharField(
        max_length=100, unique=True, help_text="Human-readable name for the agent."
    )
    # Local path to agent definition root
    definition_path = models.FilePathField(allow_folders=True, allow_files=True)
    definition_path = models.FileField(upload_to=None, max_length=100)

    def get_absolute_url(self):
        return reverse("agent-detail", args=[str(self.id)])
    
    def __str__(self):
        return self.name
    

class Endpoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Human-readable name, device hostname, and remote address
    # Does this device actually have an agent installed?
    is_virtual = models.BooleanField()
    # What protocol and agent does this endpoint use, if any?
    # Also, block endpoints from destruction if an agent or protocol is deleted
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name="endpoints")
    protocols = models.ManyToManyField(
        Protocol, related_name="endpoints"
    )
    # Additional JSON configuration object
    agent_cfg = models.JSONField(blank=True, null=True)
    # What other endpoints does this endpoint have direct access to?
    upstream_connections = models.ManyToManyField("self")
    downstream_connections = models.ManyToManyField("self")
    

class Task(models.Model):
    # What user and endpoint, if any, is this task associated with?
    # Theoretically, every task was caused by *someone*, even if it's
    # a periodic task
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="tasks")
    # When was this task started/finished?
    end_time = models.DateTimeField(blank=True, null=True)
    # Arbitrary data that may be associated with the task. Should be plaintext.
    data = models.TextField(blank=True, null=True)
    

class TaskResult(models.Model):
    # Arbitrary data field; may contain files, a raw message, etc. (Note that
    # if a file is present, it *should* be stored with File and not this field.)
    data = models.BinaryField(blank=True, null=True)


class Log(models.Model):
    # Enum field, levels are likely to be 0 - 5
    level = models.IntegerField(blank=True, null=True)