from django.db.models import fields
from rest_framework import serializers
from bd_client.models import Firstname, Lastname, Surname, Persons

class PersonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persons
        fields = '__all__'

class FirstnameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firstname
        fields = '__all__'

class LastnameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lastname
        fields = '__all__'

class SurnameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surname
        fields = '__all__'
