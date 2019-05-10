import graph
from dijkstras import dijkstra
import priority_queue
graph=graph.graph

def result():
    input_graph=[]
    file_inp=open("in.in","r")
    vert_edge=file_inp.readline().split()
    n_vertices=int(vert_edge[0])
    n_edges=int(vert_edge[1])
    network=graph(n_vertices,n_edges)
    for _ in range(n_edges):
        inp=file_inp.readline().split()
        from_edge=inp[0]
        to_edge=inp[1]
        weight=int(inp[2])
        input_graph.append([inp[0],inp[1],inp[2]])
        network.addEdge(from_edge,to_edge,weight)

    source_dest=file_inp.readline().split()
    source_router=source_dest[0]
    destination_router=source_dest[1]
    network.set_source_dest(source_router,destination_router)
    queue=priority_queue.priority_queue()

    dist,prev,steps =dijkstra(network,queue)
    # print(steps)
    return(steps,dist,prev,input_graph)

if __name__ == "__main__":
    result()   