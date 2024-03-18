from collections import deque

graph = {'1': ['2', '3'],
         '2': ['4', '5'],
         '3': ['6', '7'],
         '4': [],
         '5': [],
         '6': [],
         '7': []
         }
visitedNodes = []
queue = []



def bfs (graph, visitedNodes,node):
    visitedNodes.append(node)
    queue.append(node)

    while queue :
        m = queue.pop(0)
        print(m, end="")

        for i in graph[m]:
            if i not in visitedNodes:
                visitedNodes.append(i)
                queue.append(i)

print("following in bfs ")
bfs(graph,visitedNodes,'1')