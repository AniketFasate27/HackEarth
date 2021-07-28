def initial_graph() :
    
    return tuple (
            
         {1, 2,30},
         {1,3,10},
         {2,5,40},
         {3,4,20},
         {4,5,30} 
    )



print(initial_graph())
    

initial = 1

path = {}

adj_node = {}

queue = []

graph = initial_graph()

for node in graph:
    path[node] = float("inf")
    adj_node[node] = None
    queue.append(node)
    
path[initial] = 0

while queue:
    # find min distance which wasn't marked as current
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]  
            min_val = path[key_min]
    cur = key_min
    queue.remove(cur)
    print(cur)
    

    for i in graph[cur]:
        alternate = graph[cur][i] + path[cur]
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = cur
            
            
x = 5
print('The path between A to H')
print(x, end = '<-')
while True:
    x = adj_node[x]
    if x is None:
        print("")
        break
    print(x, end='<-')