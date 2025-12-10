from task_1_graph import edges
from task_2 import build_adj_list

# Алгоритм Дейкстри, повертає і відстані, і попередників
def dijkstra_with_paths(graph, start):
    distances = {v: float('infinity') for v in graph}
    previous = {v: None for v in graph}

    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current] == float('infinity'):
            break

        for neighbor, w in graph[current].items():
            distance = distances[current] + w
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current

        visited.append(current)
        unvisited.remove(current)

    return distances, previous

# Відновлює маршрут від start до end
def reconstruct_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    else:
        return None

# Запускає Дейкстру для кожної вершини та повертає всі маршрути
def all_pairs_shortest_paths(graph):
    result = {}

    for start in graph:
        distances, previous = dijkstra_with_paths(graph, start)

        result[start] = {}

        for end in graph:
            path = reconstruct_path(previous, start, end)
            result[start][end] = {
                "distance": distances[end],
                "path": path
            }

    return result


if __name__ == "__main__":
     graph = build_adj_list(edges)
     apsp = all_pairs_shortest_paths(graph)

     # Bивести всі маршрути для конкретної станції, наприклад, Sherbrooke
     for dest, info in apsp["Sherbrooke"].items():
         dist = info["distance"]
         path = info["path"]
         if dist != float('infinity'):
             print(f"{'Sherbrooke -> ' + dest:<40} | {dist:.2f} | {path}")
         else:
             print(f"{'Sherbrooke -> ' + dest:<40} | недосяжно")
