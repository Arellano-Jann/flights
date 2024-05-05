import uuid
import datetime

from django.contrib.auth.models import User, Group
from django.db import models
from django.urls import reverse
from django.conf import settings


class City(models.Model):
    code = models.CharField(primary_key=True, editable=False, max_length=6) # City Code
    name = models.CharField(blank=True, null=True, max_length=255) # City Name
    
    
class Airline(models.Model):
    iata_code = models.UUIDField(primary_key=True, editable=False, max_length=2, help_text="Enter airport's unique IATA code") # Standardized 2 CHAR IATA Code
    name = models.TextField(blank=True, null=True) # Airline Name


class Airport(models.Model):
    iata_code = models.CharField(primary_key=True, editable=False, max_length=3, help_text="Enter airline's unique IATA code") # Standardized 3 CHAR IATA Code
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="airports") # City that Airport is in
    airline = models.ManyToManyField(Airline, related_name="airports") # Airlines that the airport services.
    
    
class Aggregator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(blank=True, null=True) # Aggregator Source Name


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    min_cost = models.IntegerField(help_text="Minimum cost for the flight")
    max_cost = models.IntegerField(help_text="Maximum cost for the flight")
    avg_cost = models.IntegerField(blank=True, null=True, help_text="Average cost for the flight. If empty, this is autofilled.")
    
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name="airline")

    # This can be extended into a dropdown list of values and autopopulated.
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="from_airport", help_text="Enter three letter airport location ID") # 
    to_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="to_airport", help_text="Enter three letter airport location ID") # 
    
    date_first_checked = models.DateField(blank=True, null=True, help_text="Enter in the form: ")
    date_last_checked = models.DateField(blank=True, null=True, help_text="Enter in the form: ")
    date_of_flight = models.DateField(blank=True, null=True, help_text="Enter the day the plane flies out") # note that this not consider return flights and those would have to be entered again
    days_of_the_week = [("Monday","Monday"), ("Tuesday","Tuesday"), ("Wednesday","Wednesday"), ("Thursday","Thursday"), ("Friday","Friday"), ("Saturday","Saturday"), ("Sunday","Sunday")]
    day_of_flight = models.CharField(blank=True, max_length=9, choices=days_of_the_week, help_text="i.e. Monday")

    def get_absolute_url(self):
        return reverse("flight-detail", args=[str(self.id)])
    
    def __str__(self):
        return self.date_of_flight + ': ' + self.from_airport + ' to ' + self.to_airport
    

class Agg_Flights(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aggregator = models.ForeignKey(Aggregator, on_delete=models.CASCADE, related_name="aggregator") # Aggregator
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="flight") # City that Airport is in
    
    
class Historical_Data(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    min_cost = models.IntegerField(help_text="Minimum cost for the flight")
    max_cost = models.IntegerField(help_text="Maximum cost for the flight")
    avg_cost = models.IntegerField(blank=True, null=True, help_text="Average cost for the flight. If empty, this is autofilled.")
    
    # Contains data about when it was obtained, the flight 
    date_checked = models.DateField(blank=True, null=True, help_text="Enter in the form: ")
    date_of_flight = models.DateField(blank=True, null=True, help_text="Enter the day the plane flies out") # note that this not consider return flights and those would have to be entered again
    days_of_the_week = [("Monday","Monday"), ("Tuesday","Tuesday"), ("Wednesday","Wednesday"), ("Thursday","Thursday"), ("Friday","Friday"), ("Saturday","Saturday"), ("Sunday","Sunday")]
    day_of_flight = models.CharField(blank=True, max_length=9, choices=days_of_the_week, help_text="i.e. Monday")
    
    