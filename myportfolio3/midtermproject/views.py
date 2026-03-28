from django.shortcuts import render
from .models import Skills

def midtermproject(request):
  skills = Skills.objects.all()
  context = {'skills':skills}

  return render(request, 'home.html', context)