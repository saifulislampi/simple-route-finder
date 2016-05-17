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

    context={
        "form":form
    }


    if "submit" in request.POST:
        source_id=request.POST.get("source")
        destination_id=request.POST.get("destination")
        try:
            source=stopages.get(id=source_id)
            destination=stopages.get(id=destination_id)
        except:
            return render(request,"index.html",context)

        priority=request.POST.get("priority")

        e_objects,total=shortest_distance(source,destination,stopages,edges,priority)

        for e in e_objects:
            for bus in e.busoption_set.all():
                print bus.bus_name

        context={
            "form":form,
            "result":True,
            "map": True,
            "total": total,
            "e_objects": e_objects,
            "default": True,
            "cost": False,
            "origin":source.name+" Bus Stop",
            "destination":destination.name+" Bus Stop",

        }

        if(priority=="cost"):
            context["cost"]=True
            context["default"]=False



        return render(request,"index.html",context)



    return render(request,"index.html",context)
