from django.urls import path, include
from flights import views
# from flights.views import *
# from flights.views import CredentialViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'flights', views.FlightViewSet, basename='flights')
router.register(r'signUp', views.SignUpViewSet, basename='signUp')

urlpatterns = [
    # path('/', views.credentials),
    # path(r'^', include(router.urls)),
    path('/', include(router.urls)),
    # path('/signUp/', views.signUp),
    # path('/signUpGeneric/', views.SignUpView.as_view(), name='signupgeneric'),
    # path('/credentials', views.credentials), # rememeber that this is backend/credentials on the server
    # path('/addCredential/', views.addCredential)
]
