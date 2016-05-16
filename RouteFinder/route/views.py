from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BusOption,Edge,Stopage
from .forms import RouteForm
import heapq
import sys

# Create your views here.
edges=Edge.objects.all()
stopages=Stopage.objects.all()


def shortest_distance(source, destination):
    print "Source: "+source.name
    print "Destination: "+destination.name


    cost={}
    visited={}
    previous={}


    for stopage in stopages:
        cost[stopage]=sys.maxint
        visited[stopage]=False
        previous[stopage]=None

    cost[source]=0;

    s=stopages.get(id=source.id)
    print("Cost of before loop : "+s.name+" "+str(cost[s]))



    unvisited_queue = [(cost[v],v) for v in stopages]
    heapq.heapify(unvisited_queue)
    # print(unvisited_queue)


    while len(unvisited_queue):
    #     # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        visited[current]=True


        print("Cost of "+current.name+" is : "+str(cost[current]))

        adjacent=current.adjacent.all()
        
        for next in adjacent:
            # if visited, skip
            if visited[next]:
                continue
            try:
                edge=edges.get(source=current,dest=next)
            except:
                edge=edges.get(source=next,dest=current)

            print(current.name+" : "+next.name)
            print(edge.source.name+" >>> "+edge.dest.name)

            new_cost = cost[current] + edge.distance

            if new_cost < cost[next]:
                print("New cost of "+next.name+" :"+str(new_cost))
                cost[next]=new_cost
                previous[next]=current

            else:
                pass
    #           print("Nothing happend here...")
    #
    #     # Rebuild heap
    #     # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
    #     # 2. Put all vertices not visited into the queue
        unvisited_queue = [(cost[v],v) for v in stopages if not visited[v]]
        heapq.heapify(unvisited_queue)


    print("Final cost of destination is :"+str(cost[destination]))






def home(request):

    if "submit" in request.POST:
        source_id=request.POST.get("source")
        destination_id=request.POST.get("destination")

        source=stopages.get(id=source_id)
        destination=stopages.get(id=destination_id)

        shortest_distance(source,destination)



    form=RouteForm()
    context={
        "title":"Home",
        "form":form
    }



    return render(request,"base.html",context)
