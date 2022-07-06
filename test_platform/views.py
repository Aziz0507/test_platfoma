from django.shortcuts import render
from .models import *

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


def test(request, pk):
    question = Test_question.objects.all()
    content = {'test':question}
    return render(request, 'tests.html', content)