class Node:

    # Initialize the class
    def __init__(self, name:str, elements:dict, h:int, parent):
        self.name = name
        self.elements = elements
        self.h = h 
        self.parent = parent

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
         return self.h < other.h

def BFS(graph:dict, heuristics:dict, start:str, end:str):
    
    remaining = []
    visited = []

    startNode = Node(start, graph[start], heuristics[start], None)
    endNode =  Node(end, graph[start], heuristics[end], None)

    remaining.append(startNode)
    
    while len(remaining) > 0:

        remaining.sort()
        currentNode = remaining.pop(0)
        visited.append(currentNode)

        if currentNode == endNode:
            path = []

            while currentNode != startNode:
                path.append(currentNode.name + ': ' + str(currentNode.h))
                parentNode = currentNode.parent
                currentNode = Node(parentNode.name, graph[parentNode.name], heuristics[parentNode.name], parentNode.parent)
 
            path.append(startNode.name + ': ' + str(startNode.h))
            return path[::-1]

        neighbors = currentNode.elements

        for key, value in neighbors.items():

            neighbor = Node(key, graph[key], heuristics[key], currentNode)

            if neighbor in visited or neighbor in remaining:
                continue

            remaining.append(neighbor)

    return None



graph = {   
            "Arad":{"Zerind":75,"Timisoara":118,"Sibiu":140},
            "Bucharest":{"Fagaras":211,"Urziceni":85,"Giurgiu":90,"Pitesti":101},
            "Craiova":{"Dobreta":120,"Rimnicu Vilcea":146,"Pitesti":138},
            "Dobreta":{"Mehadia":75,"Craiova":120},
            "Eforie":{"Hirsova":86},
            "Fagaras":{"Bucharest":211,"Sibiu":99},
            "Giurgiu":{"Bucharest":90},
            "Hirsova":{"Eforie":86},
            "Iasi":{"Neamt":87,"Vaslui":92},
            "Lugoj":{"Timisoara":111,"Mehadia":70},
            "Mehadia":{"Dobreta":75,"Lugoj":70},
            "Neamt":{"Iasi":87},
            "Oradea":{"Zerind":71,"Sibiu":151},
            "Pitesti":{"Rimnicu Vilcea":97,"Bucharest":101},
            "Rimnicu Vilcea":{"Sibiu":80,"Pitesti":97},
            "Sibiu":{"Fagaras":99,"Oradea":151,"Arad":140,"Rimnicu Vilcea":80},
            "Timisoara":{"Arad":118,"Lugoj":111},
            "Urziceni":{"Hirsova":98,"Bucharest":85},
            "Vaslui":{"Iasi":92,"Urziceni":142},
            "Zerind":{"Oradea":71,"Arad":75}
        }

heuristics = {   
            "Arad":366,
            "Bucharest":0,
            "Craiova":160,
            "Dobreta":242,
            "Eforie":161,
            "Fagaras":178,
            "Giurgiu":77,
            "Hirsova":151,
            "Iasi":226,
            "Lugoj":244,
            "Mehadia":241,
            "Neamt":234,
            "Oradea":380,
            "Pitesti":98,
            "Rimnicu Vilcea":193,
            "Sibiu":253,
            "Timisoara":329,
            "Urziceni":80,
            "Vaslui":199,
            "Zerind":374
        }

print(BFS(graph,heuristics, "Arad", "Bucharest"))