from django.urls import path, include
from .views import ContactsList, ContactDetails


urlpatterns = [
    path('api/contacts/', ContactsList.as_view()),
    path('api/contacts/<int:id>/', ContactDetails.as_view())
]