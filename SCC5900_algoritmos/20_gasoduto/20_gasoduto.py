from collections import deque
INF = 10**10
def BFS_path(graph, source, sink): 
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True
    while queue and not visited[sink]:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    if not visited[sink]:
        return None, 0
    path = []
    v = sink
    bottleneck = INF
    while v != source:
        path.append(v)
        bottleneck = min(bottleneck, graph[parent[v]][v])
        v = parent[v]
    path.append(source)
    path.reverse()
    return path, bottleneck

def edmonds_karp(capacities, source, sink):
    n = len(capacities)
    residual = [{v: capacities[u][v] for v in capacities[u]} for u in range(n)]
    max_flow = 0

    while True:
        path, bottleneck = BFS_path(residual, source, sink)
        if path is None:
            break
        max_flow += bottleneck
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            residual[u][v] = residual[u].get(v, 0) - bottleneck
            residual[v][u] = residual[v].get(u, 0) + bottleneck
    return max_flow


if __name__ == "__main__":
    n, m = map(int, input().split())
    capacities = [{} for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        capacities[a-1][b-1] = capacities[a-1].get(b-1, 0) + c
    print(edmonds_karp(capacities, 0, n-1) if n > 1 else 0)