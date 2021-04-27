from django.shortcuts import render
from .models import Contacts
from .serializers import ContactsSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView

class ContactsList(APIView):
    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetails(APIView):
    def get_object(self,id):
        try:
            return Contacts.objects.get(id=id)

        except Contacts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        contacts = self.get_object(id)
        serializer = ContactsSerializer(contacts)
        return Response(serializer.data)

    def put(self, request, id):
        contacts = self.get_object(id)
        serializer = ContactsSerializer(contacts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        contact = self.get_object(id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


