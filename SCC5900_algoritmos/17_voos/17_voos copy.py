def DFS(v, visited, voos):
    visited[v] = True
    for i in voos[v]:
        if not visited[i]:
            DFS(i, visited, voos)

def BFS(v, visited, voos):
    visited[v] = True
    queue = [v]
    while queue:
        v = queue.pop(0)
        for i in voos[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

if __name__ == "__main__":
    n, m = map(int, input().split())
    # distances = [n * [INF] for _ in range(n)]
    voos = [[] for i in range(n)]
    reversos = [[] for i in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        if b-1 not in voos[a-1]:
            voos[a-1].append(b-1)
            reversos[b-1].append(a-1)
    visited = [False]*n
    BFS(0, visited, voos)
    if False in visited:
        print("NAO")
        exit()
    visited = [False]*n
    BFS(0, visited, reversos)
    if False in visited:
        print("NAO")
    else:
        print("SIM")
