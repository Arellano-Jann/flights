# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions, viewsets
from django.contrib.auth.models import User
from flights.models import Flight
from flights.serializers import SignUpSerializer, FlightSerializer
# from flights import models
# from flights import serializers

# Create your views here.
# Users
# @api_view(['POST'])
# def signUp(request):
#     serializer = SignUpSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(data=serializer.data)

# from rest_framework import generics
# class SignUpView(generics.GenericAPIView):
#     serializer_class = SignUpSerializer
#     def post(self, request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "User created",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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


# Agents
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
@api_view(['GET'])
def agents(request):
    agents = Agent.objects.all()
    serializer = AgentSerializer(agents, many=True) # setting to true means to serialize multiple items. False is just one item
    return Response(serializer.data)

@api_view(['POST'])
def addAgent(request):
    serializer = AgentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Credentials
class CredentialViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    
    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return self.get_paginated_response(self.paginate_queryset(serializer.data))

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass