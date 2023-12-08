from django.urls import path, include
from flights import views
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
]
