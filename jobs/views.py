from django.shortcuts import render
from django.http import HttpResponse

from .form import jobCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/user:login')
def create_job(request):
    if request.method == 'POST':
        form = jobCreationForm(request.POST)
        if not form.is_valid():
            return HttpResponse("some of your data is not valid")
        form.save()
        
    form = jobCreationForm()
    return render(request,'jobform.html',{"form":form})
