# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, permissions, viewsets
from django.contrib.auth.models import User
from flights.models import (
    City, 
    Airline,
    Airport,
    Aggregator,
    Flight,
    AggFlight,
    HistoricalData,
    )
from flights.serializers import (
    SignUpSerializer,
    CitySerializer, 
    AirlineSerializer,
    AirportSerializer,
    AggregatorSerializer,
    FlightSerializer,
    AggFlightSerializer,
    HistoricalDataSerializer,
    )
from flights.flight_api import skiplagged

    
class SignUpViewSet(viewsets.ViewSet):
    serializer_class = SignUpSerializer
    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(data=serializer.data)
    
    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User created",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Citys
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Airlines
class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

# Airports
class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

# Aggregators
class AggregatorViewSet(viewsets.ModelViewSet):
    queryset = Aggregator.objects.all()
    serializer_class = AggregatorSerializer

# Flights
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# AggFlights
class AggFlightViewSet(viewsets.ModelViewSet):
    queryset = AggFlight.objects.all()
    serializer_class = AggFlightSerializer

# HistoricalDatas
class HistoricalDataViewSet(viewsets.ModelViewSet):
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer
    
class APIViewSet(viewsets.ViewSet):
    # Used so that it shows up in DRF routers
    def list(self, request):
        return Response()
    
    # breaks the get by having side effects
    @action(detail=False, methods=['get'])
    def get_skiplagged_data(self, request):
        skiplagged_api = skiplagged.Skiplagged()
        skiplagged_search = skiplagged_api.search(offset=True)
        lowest_priced_flights = skiplagged_api.get_lowest_price(100)
        
        for key, value in lowest_priced_flights.items():
            one_way_price = value.get('one_way_price')
            from_source = value.get('from_source')
            to_dest = value.get('to_dest')
            date_checked = value.get('date_checked')
            
            airline = value.get('airline')
            flight_numbers = value.get('flight_number')
            flight_date = value.get('flight_date')
        
            Airline.objects.get_or_create(iata_code=airline)
            Airport.objects.get_or_create(iata_code=from_source)
            Airport.objects.get_or_create(iata_code=to_dest)
            Flight.objects.get_or_create(
                min_cost=one_way_price,
                max_cost=one_way_price,
                avg_cost=one_way_price,
                airline=Airline.objects.get(iata_code=airline),
                from_airport=Airport.objects.get(iata_code=from_source),
                to_airport=Airport.objects.get(iata_code=to_dest),
                date_first_checked=date_checked,
                date_last_checked=date_checked,
                date_of_flight=flight_date,
            )
            HistoricalData.objects.get_or_create(
                min_cost=one_way_price,
                max_cost=one_way_price,
                avg_cost=one_way_price,
                date_checked=date_checked,
                date_of_flight=flight_date,
            )
        
        Aggregator.objects.get_or_create(name='Skiplagged')
        
        return Response(lowest_priced_flights)
        
        



# # Credentials
# class CredentialViewSet(viewsets.ModelViewSet):
#     queryset = Credential.objects.all()
#     serializer_class = CredentialSerializer
    
#     # def list(self, request):
#     #     serializer = self.get_serializer(self.get_queryset(), many=True)
#     #     return self.get_paginated_response(self.paginate_queryset(serializer.data))

#     # def create(self, request):
#     #     pass

#     # def retrieve(self, request, pk=None):
#     #     pass

#     # def update(self, request, pk=None):
#     #     pass

#     # def partial_update(self, request, pk=None):
#     #     pass

#     # def destroy(self, request, pk=None):
#     #     pass