from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import TestSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# from .forms import Test_quest_form



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
        

def Quiz(request, pk):
    # form  = Test_quest_form()
    model = Test_question.objects.filter(test_type_id = pk)
    content = {'quiz': model}

    if request.method == 'POST' and request.is_ajax():
        asd = request.POST('')
        if asd.is_validate():
            asd.save()
            return render(request, 'quiz.html')
        else:
            return JsonResponse(status = 400)
        




    # return render(request, 'quiz.html', content)

def Answer(request):
    Verifity = Verifity_Models.objects.all()
    Quest = Test_question.objects.filter()

    for ver in Verifity:
        for quest in Quest:
            if ver.option_user == quest.answer:
                asd = {'test':'good'}
                return 'Good'
            else:
                asd = {'test':'ill'}
                return 'ты ошибся'


    return render(request, 'answer.html', asd)
