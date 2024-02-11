UP, RIGHT, DOWN, LEFT = (0, -1), (1, 0), (0, 1), (-1, 0) 

def maze_to_graph(maze):
    vertices = set(maze)
    edges = set()
    weights = {}
    for vertex in vertices:
        x, y = vertex
        for (dx, dy) in [UP, RIGHT, DOWN, LEFT]:
            neighbor = (x + dx, y + dy)
            if neighbor in vertices:
                edge = (vertex, neighbor)
                edges.add(edge)
                weights[edge] = 1
    return (vertices, edges, weights)
