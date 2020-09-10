from django.shortcuts import render
from .models import Datatest
# Create your views here.
def index(request):
    datatest = Datatest.objects.all()
    return render(request, 'polls/index.html', {'datatest':datatest})
    
def data(request, question_id):
    datatest = Datatest.objects.all()
    return render(request, 'polls/data.html', {'datatest':datatest, 'question_id':question_id})