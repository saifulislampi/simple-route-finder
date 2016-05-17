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

        adjacent=current.adjacent.all()

        for next in adjacent:
            # if visited, skip
            if visited[next]:
                continue
            try:
                edge=edges.get(source=current,dest=next)
            except:
                edge=edges.get(source=next,dest=current)

            # print(current.name+" : "+next.name)
            # print(edge.source.name+" >>> "+edge.dest.name)

            new_cost = cost[current] + weight[edge]

            if new_cost < cost[next]:
                # print("New cost of "+next.name+" :"+str(new_cost))
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

    total=cost[destination]
    print("Final cost of destination is :"+str(total))

    #Preparing for web output

    E_Objects=[] #Edges in our path


    #Re order the path
    x=destination
    while(previous[x]):
        p=previous[x]
        next_to[p]=x
        x=previous[x]

    next_to[destination]=None;

    s=source;
    while(next_to[s]):
        try:
            e=edges.get(source=s,dest=next_to[s])
        except:
            e=edges.get(dest=s,source=next_to[s])
            e.source=s;
            e.dest=next_to[s]

        E_Objects.append(e);
        s=next_to[s]


    return E_Objects,total
