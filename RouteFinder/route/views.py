from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BusOption,Edge,Stopage
from .forms import RouteForm
import heapq
import sys
from .routefinder import shortest_distance

stopages=Stopage.objects.all()
edges=Edge.objects.all()


def home(request):
    form=RouteForm()

    if "submit" in request.POST:
        source_id=request.POST.get("source")
        destination_id=request.POST.get("destination")

        source=stopages.get(id=source_id)
        destination=stopages.get(id=destination_id)

        priority=request.POST.get("priority")

        path=shortest_distance(source,destination,stopages,edges,priority)

        d={}
        d["5"]="Hello";
        context={
            "title":"Home",
            "form":form,
            "path":path,
            "d":stopages,
        }

        return render(request,"index.html",context)




    context={
        "title":"Home",
        "form":form
    }


    return render(request,"index.html",context)
