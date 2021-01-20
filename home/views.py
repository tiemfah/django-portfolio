from django.http import HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render
from .models import Message
from .forms import MessageForm

# Create your views here.
def index(request):
  form = MessageForm()
  return render(request, 'home/index.html', {'form': form})

def message(request):
  form = MessageForm()
  new_message = Message.objects.create(email=request.POST['email'], message=request.POST['message'])
  return render(request, 'home/index.html', {'form': form})
