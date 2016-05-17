from .models import BusOption,Edge,Stopage
import heapq
import sys




def shortest_distance(source, destination,stopages,edges,priority=None):
    print "Source: "+source.name
    print "Destination: "+destination.name


    cost={}
    visited={}
    previous={}
    weight={}
    next_to={}

    if priority=="distance":
        for edge in edges:
            weight[edge]=edge.distance

    elif priority=="time":
        for edge in edges:
            weight[edge]=edge.distance*edge.jam_factor

    elif priority=="cost":
        for edge in edges:
            weight[edge]=edge.best_option.cost

    else:
        for edge in edges:
            weight[edge]=edge.distance



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

        if(current==destination):
            break

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

            new_cost = cost[current] + weight[edge]

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

    x=destination
    path=" --END"



    while(previous[x]):
        try:
            edge=edges.get(source=x,dest=previous[x])
        except:
            edge=edges.get(dest=x,source=previous[x])
        path="--"+str(weight[edge])+ "--"+x.name+path;

        
        x=previous[x]

    path=source.name+path
    print(path)

    return path;
