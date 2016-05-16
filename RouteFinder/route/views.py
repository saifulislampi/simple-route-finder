from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BusOption,Edge,Stopage
from .forms import RouteForm
# Create your views here.


def home(request):

    if "submit" in request.POST:
        source_id=request.POST.get("source")
        destination_id=request.POST.get("destination")

        



    form=RouteForm()
    context={
        "title":"Home",
        "form":form
    }

    return render(request,"base.html",context)
