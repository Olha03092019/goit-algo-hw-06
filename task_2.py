from collections import deque
from task_1_graph import edges

# Створення списку суміжності
def build_adj_list(elements):
    new_graph = {}
    for u, v, w in elements:
        new_graph.setdefault(u, []).append(v)
        new_graph.setdefault(v, []).append(u)
    return new_graph

# Рекурсивний DFS
def dfs_recursive(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, path)

    return path

# Рекурсивний BFS
def bfs_recursive(graph, queue, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if not queue:
        return path

    vertex = queue.popleft()

    if vertex not in visited:
        visited.add(vertex)
        path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

    return bfs_recursive(graph, queue, visited, path)


if __name__ == "__main__":
     graph = build_adj_list(edges)
     start_node = "Berri-UQAM"

     print("\nDFS шлях:")
     dfs_path = dfs_recursive(graph, start_node)
     print(" -> ".join(dfs_path))

     print("\nBFS шлях:")
     bfs_path = bfs_recursive(graph, deque([start_node]))
     print(" -> ".join(bfs_path))

