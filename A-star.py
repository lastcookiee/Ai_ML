import math

class Node:
    def __init__(self,name,heuristic=0):
        self.name=name
        self.heuristic=heuristic
        self.g = float('inf')
        self.f = float('inf')
        self.came_from = None

    def __repr__(self):
        return f'{self.name}'

def astar(graph, start_node, goal_node):
    open_list=[start_node]
    closed_list=set()

    start_node.g = 0
    start_node.f = start_node.heuristic

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)

        if current_node == goal_node:
            return reconstruct_path(current_node)

        open_list.remove(current_node)
        closed_list.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor in closed_list:
                continue
                
            tentative_g_score = current_node.g + cost

            if tentative_g_score < neighbor.g:
                neighbor.came_from = current_node
                neighbor.g = tentative_g_score
                neighbor.f = neighbor.g + neighbor.heuristic

                if neighbor not in open_list:
                    open_list.append(neighbor)
    
    return None


def reconstruct_path(node):
    path=[]
    current = node
    while current is not None:
        path.append(current.name)
        current = current.came_from
    return path[::-1]

def euclidean_distance(node_a, node_b, coordinates):
    x1, y1 = coordinates[node_a.name]
    x2, y2 = coordinates[node_b.name]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def setup_graph():
    coordinates = {
        'A': (0, 0),
        'B': (1, 2),
        'C': (4, 2),
        'D': (5, 5),
        'E': (7, 1),
        'F': (9, 5),
        'G': (10, 0)
    }

    nodes = {name: Node(name) for name in coordinates}
    goal_node = nodes['G']
    for node in nodes.values():
        node.heuristic = euclidean_distance(node, goal_node, coordinates)

    graph = {
        nodes['A']: {nodes['B']: 2, nodes['C']: 4},
        nodes['B']: {nodes['A']: 2, nodes['D']: 5, nodes['C']: 3},
        nodes['C']: {nodes['A']: 4, nodes['B']: 3, nodes['E']: 3},
        nodes['D']: {nodes['B']: 5, nodes['F']: 2},
        nodes['E']: {nodes['C']: 3, nodes['G']: 3},
        nodes['F']: {nodes['D']: 2, nodes['G']: 1},
        nodes['G']: {nodes['E']: 3, nodes['F']: 1},
    }

    return graph, nodes['A'], nodes['G']


graph,start,goal = setup_graph()
path = astar(graph,start,goal)

if path:
    print("Path found:", path)
else:
    print("No path found")