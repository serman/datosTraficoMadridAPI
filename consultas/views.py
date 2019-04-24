from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet, ViewSet
from rest_framework import serializers
from consultas.serializers import  BasicQuerySerializer, MedidorDataSerializer, MedidorData
# Create your views here.
from .visordatostraficomadrid import api
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class basicQueryViewSet(ViewSet):
    serializer_class = MedidorDataSerializer

    # http://127.0.0.1:8000/query/?id_medidor=4418&year1=2017&month1=10&day1=1&hour1=0&year2=2017&month2=10&day2=30&hour2=0&format=json
    # http://127.0.0.1:8000/query/?id_medidor=4418&year1=2017&month1=10&day1=1&hour1=0&year2=2017&month2=10&day2=30&hour2=0&format=json
    def list(self, request):
        ### parse parameters ####
        print(request.query_params)
        _id_medidor = self.request.query_params.get('id_medidor', None)
        _year1 = self.request.query_params.get('year1', None)
        _month1 = self.request.query_params.get('month1', None)
        _day1 = self.request.query_params.get('day1', None)
        _hour1 = self.request.query_params.get('hour1', None)

        _year2 = self.request.query_params.get('year2', None)
        _month2 = self.request.query_params.get('month2', None)
        _day2 = self.request.query_params.get('day2', None)
        _hour2 = self.request.query_params.get('hour2', None)

        _by15minutes = self.request.query_params.get('by15minutes', False)

        if(_id_medidor==None  or _year1==None or _month1 == None or _day1 == None  or _hour1==None or _year2==None or _month2 == None or _day2 == None  or _hour2==None  ):
            return Response({'error': "mising input parameter"})

        _id_medidor=int(_id_medidor)
        _year1=int(_year1)
        _month1=int(_month1)
        _day1=int(_day1)
        _hour1=int(_hour1)
        _year2=int(_year2)
        _month2=int(_month2)
        _day2=int(_day2)
        _hour2=int(_hour2)
        ### ACTUAL QUERY ####
        #resultstr, medidor_id = api.medidorPeriodo(4418, 2017, 10, 1, 0, 2017, 10, 4, 0, False)
        _by15minutes=bool(_by15minutes)
        resultstr, medidor_id = api.medidorPeriodo(_id_medidor, _year1, _month1, _day1, _hour1, _year2, _month2, _day2, _hour2, _by15minutes)
#outputStr += (f"El medidor {medidor3} el día {j[3]} del mes {j[2]} del año {j[1]} a las {j[4]} horas y {j[5]} minutos tuvo unas mediciones de {j[7]} intensidad, {j[8]} ocupación, {j[9]} carga y {j[10]} velocidad media")
        serializedobjects=[]
        for j in resultstr:
            line = MedidorData( medidor_id,j[3],j[2],j[1],j[4],j[5],j[7],j[8],j[9],j[10] )
            serializedline=MedidorDataSerializer(line)
            serializedobjects.append(serializedline.data)

        #print (resultstr)
        #jsonresponse+=json
        return Response({'result': serializedobjects})
