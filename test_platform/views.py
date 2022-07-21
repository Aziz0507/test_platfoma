from django import views
from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import TestSerializer, User_Test_Serializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# from .forms import Test_quest_form
from django.contrib.auth.models import User




# Create your views here.
def main(request):
    categories  = Catigoriy.objects.all()
    contetn = {'categories': categories}
    return render(request, 'index.html', contetn)


def buttons(request,pk):
    Types = Test_Types.objects.filter(types_catigoriy_id = pk)
    contetn = {'thems': Types}
    if pk == 1:
        return render(request, 'computer_sciens.html', contetn)
    elif pk == 2:
        return render(request, 'program.html', contetn)


class TestApiViews(generics.ListAPIView):
    # print('до функции')
    queryset = Test_question.objects.all()
    serializer_class = TestSerializer
   
    # @api_view(['POST', 'GET'])

    
    def list(self,request, pk):
        queryset = self.get_queryset().filter(test_type_id = pk)
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = TestSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class user_test_views(ModelViewSet):
    queryset         = Verifity_Models.objects.all()
    serializer_class = User_Test_Serializer

    # @action(method = 'put', detail = False)
    def update(self, request):
        objects = self.get_object()
        serializer = User_Test_Serializer(data = request.data)
        if serializer.is_valid():
            objects.update(serializer.validated_data['quest'])

        

def Quiz(request, pk):
    # form  = Test_quest_form()
    model = Test_question.objects.filter(test_type_id = pk)
    users_as = User.objects.all()
    content = {'quiz': model}
    return render(request, 'quiz.html',content)


        




    # return render(request, 'quiz.html', content)

def Answer(request):
    Verifity = Verifity_Models.objects.all()
    Quest = Test_question.objects.filter()

    
    if request.method == 'POST' and request.is_ajax():
        asd = request.POST('Question')
        if asd.is_validate():
            asd.save()
            return render(request, 'answer.html', asd)

        else:
            return JsonResponse(status = 400)

