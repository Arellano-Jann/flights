from django.urls import path, include
from flights import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cities', views.CityViewSet, basename='cities')
router.register(r'airlines', views.AirlineViewSet, basename='airlines')
router.register(r'airports', views.AirportViewSet, basename='airports')
router.register(r'aggregators', views.AggregatorViewSet, basename='aggregators')
router.register(r'flights', views.FlightViewSet, basename='flights')
router.register(r'aggflights', views.AggFlightViewSet, basename='aggflights')
router.register(r'historicaldata', views.HistoricalDataViewSet, basename='historicaldata')
router.register(r'api', views.APIViewSet, basename='api')
router.register(r'signUp', views.SignUpViewSet, basename='signUp')

urlpatterns = [
    # path('/', views.credentials),
    # path(r'^', include(router.urls)),
    path('/', include(router.urls)),
    # path('/signUp/', views.signUp),
    # path('/signUpGeneric/', views.SignUpView.as_view(), name='signupgeneric'),
]
