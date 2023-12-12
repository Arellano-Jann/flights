import uuid
import datetime

from django.contrib.auth.models import User, Group
from django.db import models
from django.urls import reverse
from django.conf import settings


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    min_cost = models.IntegerField(help_text="Minimum cost for the flight")
    max_cost = models.IntegerField(help_text="Maximum cost for the flight")
    avg_cost = models.IntegerField(blank=True, null=True, help_text="Average cost for the flight. If empty, this is autofilled.")

    # This can be extended into a dropdown list of values and autopopulated. However it's manual currently
    from_city = models.TextField(blank=True, null=True, help_text="Enter source city name")
    to_city = models.TextField(blank=True, null=True, help_text="Enter destination city name")
    from_airport = models.CharField(blank=True, null=True, max_length=3, help_text="Enter three letter airport location ID")
    to_airport = models.CharField(blank=True, null=True, max_length=3, help_text="Enter three letter airport location ID")
    
    airline = models.TextField(blank=True, null=True, help_text="")
    flight_code = models.TextField(blank=True, null=True, help_text="Enter airline's unique flight code")
    
    date_first_checked = models.DateField(blank=True, null=True, help_text="Enter in the form: ")
    date_last_checked = models.DateField(blank=True, null=True, help_text="Enter in the form: ")
    date_of_flight = models.DateField(blank=True, null=True, help_text="Enter the day the plane flies out") # note that this not consider return flights and those would have to be entered again
    days_of_the_week = [("Monday","Monday"), ("Tuesday","Tuesday"), ("Wednesday","Wednesday"), ("Thursday","Thursday"), ("Friday","Friday"), ("Saturday","Saturday"), ("Sunday","Sunday")]
    day_of_flight = models.CharField(blank=True, max_length=9, choices=days_of_the_week, help_text="i.e. Monday")

    def get_absolute_url(self):
        return reverse("flight-detail", args=[str(self.id)])
    
    def __str__(self):
        return self.date_of_flight + ': ' + self.from_airport + ' to ' + self.to_airport
    
# has list of airports in the city
# class City(models.Model):
#     # Human-readable name, device hostname, and remote address
#     # Does this device actually have an agent installed?
#     is_virtual = models.BooleanField()
#     # What protocol and agent does this endpoint use, if any?
#     # Also, block endpoints from destruction if an agent or protocol is deleted
#     agent = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name="endpoints")
#     protocols = models.ManyToManyField(
#         Protocol, related_name="endpoints"
#     )
#     # Additional JSON configuration object
#     agent_cfg = models.JSONField(blank=True, null=True)
#     # What other endpoints does this endpoint have direct access to?
#     upstream_connections = models.ManyToManyField("self")
#     downstream_connections = models.ManyToManyField("self")
    

# class Airport(models.Model):
#     # What user and endpoint, if any, is this task associated with?
#     # Theoretically, every task was caused by *someone*, even if it's
#     # a periodic task
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="tasks")

# class Airline(models.Model):