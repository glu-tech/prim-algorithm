class NodePrim:
    def __init__(self, value:str, father, distance:int, position:[int]):
        self.value = value
        self.father = father
        self.distance = distance
        self.position = position

    def __str__(self):
        return f'(value = {self.value} distance={self.distance} position = {self.position} \n father: {self.father} \n)'

class Queue:
    def __init__(self, position, value):
        self.position = position
        self.value = value

    def __str__(self):
        return f'position = {self.position}\nvalue = {self.value}'

def constructor_graph(func):
    def inside(graph:[[]], r, dst, queue=[]):
        graph_obj = [[]]

        for v in range(len(graph)):
            graph_obj.append([])
            for e in range(len(graph[v])):
                graph_obj[v].append(NodePrim(graph[v][e], None, 10e6, [v,e]))

        graph = graph_obj

        graph[r[0]][r[1]].distance = 0

        return func(graph, r, dst, queue)

    return inside

def constructor_queue(func):
    def inside(graph, r, dst, queue=[]):
        for v in range(len(graph)):
            for e in range(len(graph[v])):
                queue.append(Queue([v, e], graph[v][e].distance))
        
        sorted(queue, key= lambda x: x.value)

        return func(graph, r, dst, queue)

    return inside

@constructor_graph  
@constructor_queue    
def prim(graph, r, dst:[], queue=[]):
    
    while len(queue) != 0:
        minQueue = min(queue, key=lambda x: x.value)
        queue.remove(minQueue)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir in directions:
            new_i = minQueue.position[0] + dir[0]
            new_j = minQueue.position[1] + dir[1]

            if (new_i < 0 or new_j < 0) or (new_i >= len(graph) or new_j >= len(graph[new_i])):
                continue

            if graph[new_i][new_j].value < 0:
                continue

            for x in range(len(queue)):
                if (queue[x].position[0] == new_i and queue[x].position[1] == new_j) and (graph[minQueue.position[0]][minQueue.position[1]].distance < graph[new_i][new_j].distance):
                    graph[new_i][new_j].father = graph[minQueue.position[0]][minQueue.position[1]]
                    graph[new_i][new_j].distance = graph[minQueue.position[0]][minQueue.position[1]].distance + graph[minQueue.position[0]][minQueue.position[1]].value

    current = graph[dst[0]][dst[1]]

    while current:
        print(current.position)
        current = current.father

    return graph[dst[0]][dst[1]].distance

graph = [
        [1,1,1,1],
        [3,-1,-1,-1],
        [5,0,2,0],
        [8,2,8,1],
        [9,-1,-1,1]
    ]

print(prim(graph, [0,0], [4,3]))