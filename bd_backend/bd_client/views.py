from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import serializers, views, viewsets

from bd_client.models import Persons, Firstname, Lastname, Surname
from bd_client.serializers import PersonsSerializer, FirstnameSerializer, LastnameSerializer, SurnameSerializer

def index(request):
    #return render(request, 'index.html', context={})
    return HttpResponse("BD practic API")

class PersonsView(viewsets.ModelViewSet):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializer

class FirstnameView(viewsets.ModelViewSet):
    queryset = Firstname.objects.all()
    serializer_class = FirstnameSerializer

class LastnameView(viewsets.ModelViewSet):
    queryset = Lastname.objects.all()
    serializer_class = LastnameSerializer

class SurnameView(viewsets.ModelViewSet):
    queryset = Surname.objects.all()
    serializer_class = SurnameSerializer

'''
@csrf_exempt
def personsApi(request, action, id = 0):
    if request.method == 'GET':
        if action == "query":
            persons = Persons.objects.all()
            persons_serializer = PersonsSerializer(persons, many = True)
            return JsonResponse(persons_serializer.data, safe = False)
        
    elif request.method == 'POST':
        if action == "add":
            persons_data = JSONParser().parse(request)
            persons_serializer = PersonsSerializer(data = persons_data)
            if persons_serializer.is_valid():
                persons_serializer.save()
                return JsonResponse("added successfully", safe = False)
            else:
                return JsonResponse("failed to add", safe = False)
        elif action == "remove":
            persons_data = JSONParser().parse(request)
            persons = Persons.objects.get(id = persons_data['id'])
            persons_serializer = PersonsSerializer(persons, data = persons_data)
            if persons_serializer.is_valid():
                persons_serializer.save()
                return JsonResponse("updated successfully", safe = False)
            else:
                return JsonResponse("failed to update", safe = False)
'''