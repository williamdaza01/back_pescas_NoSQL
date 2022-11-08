from dataclasses import field, fields
from rest_framework import serializers
from PescaNoSql.models import Cuenca, Metodo, Pesca

class CuencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenca
        fields = ('ID_CUENCA', 
                  'NOMBRE_CUENCA')

class MetodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodo
        fields = ('ID_METODO', 
                  'NOMBRE_METODO')

class PescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesca
        fields = ('ID_PESCA',
                  'ID_CUENCA',
                  'ID_METODO',
                  'FECHA_PESCA',
                  'PESO_PESCADO')