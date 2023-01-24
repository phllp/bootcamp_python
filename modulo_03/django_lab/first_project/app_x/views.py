from django.shortcuts import render
from .forms import UserForm

def index(request):
  return render(request, 'user/index.html')

def create(request):
  if request.method == 'GET':
    form = UserForm()
    context = {
      'form': form
    }

    return render(request, 'user/create.html', context=context)
  
  elif request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      
      context = {
        'nome': form.cleaned_data['nome'],
        'telefone': form.cleaned_data['telefone'],
        'email': form.cleaned_data['email']
      }

      form.save()
    return render(request, 'user/index.html', context=context)

def update(request, user_id):
  context = {
    'id': user_id
  }
  return render(request, 'user/index.html', context=context)
