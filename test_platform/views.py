from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    categories  = Catigoriy.objects.all()
    thems       = Test_Types.objects.all()
    contetn = {'categories': categories, 'thems':thems}
    return render(request, 'index.html', contetn)


def buttons(request):
    if request.POST.get('Программирование'):
        pass
    elif request.POST.get('кампьютерная грамотность'):
        pass

