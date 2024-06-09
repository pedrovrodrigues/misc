from collections import deque

mod = 10**9 + 7
INF = 10**15

distance_source = []
distance_target = []
dp = []
voos = {}
voos_inv = {}

# class Node:
#     def __init__(self, v, distance):
#         self.v = v
#         self.distance = distance

#     def __lt__(self, other):
#         return self.distance < other.distance

# def dijkstra(V, adj, S):
#     visited = [False] * V
#     map = {}
#     q = []

#     map[S] = Node(S, 0)
#     heapq.heappush(q, Node(S, 0))

#     while q:
#         n = heapq.heappop(q)
#         v = n.v
#         distance = n.distance
#         visited[v] = True

#         adjList = adj[v]
#         for i, w in adjList.items():
#             if not visited[i]:
#                 if i not in map:
#                     map[i] = Node(v, distance + w)
#                 else:
#                     sn = map[i]
#                     if distance + w < sn.distance:
#                         sn.v = v
#                         sn.distance = distance + w
#                 heapq.heappush(q, Node(i, distance + w))

#     result = [0] * V
#     for i in range(V):
#         result[i] = map[i].distance if i in map else INF

#     return result


# def route_count(start, end, visited, price=0):
#     if start == end:
#         dp[start][1:5] = [1,0,0,True]
#         return 1, 0, 0
#     if dp[start][4]:
#         return dp[start][1:4]
#     visited[start] = True
#     # dp[start] = [dist, routes, shortest, longest, calced?]
#     for v in voos[start]:
#         if voos[start][v] + dp[start][0] > dp[v][0] or visited[v]:
#             continue
#         count, minl, maxl = route_count(v, end, visited, price+voos[start][v])
#         if count > 0:
#             dp[start][1] += count
#             dp[start][1] %= mod
#             dp[start][2] = min(dp[start][2], minl)
#             dp[start][3] = max(dp[start][3], maxl)
#     visited[start] = False
#     dp[start][4] = True
#     dp[start][2] += 1
#     dp[start][3] += 1
#     return dp[start][1], dp[start][2], dp[start][3]


def topological_sort(V, adj):
    visited = [False] * V
    stack = []
    dfs = []
    for i in range(V):
        if not visited[i]:
            dfs.append((i, False))
        while len(dfs) > 0:
            v, back = dfs.pop()
            if back:
                stack.append(v)
                continue
            if visited[v]:
                continue
            visited[v] = True
            dfs.append((v, True))
            for j in adj[v]:
                if not visited[j]:
                    dfs.append((j, False))
    return stack[::-1]

def dijkstra(V, adj, S):
    top_sort = topological_sort(V, adj)
    dists = [INF] * V
    dists[S] = 0
    predecessor = [[]] * V
    for u in top_sort:
        for v in adj[u]:
            if dists[v] > dists[u] + adj[u][v]:
                dists[v] = dists[u] + adj[u][v]
                predecessor[v] = [u]
            elif dists[v] == dists[u] + adj[u][v]:
                predecessor[v].append(u)
    return dists, predecessor

# def route_count_iter(end, visited):
#     length = distance_source[end]
#     topological_sort = []

#     for node in topological_sort:
#         depth = distance_source[node]
#         height = distance_target[node]
#         start = node
#         if node == end:
#             dp[node] = [1,0,0]
#             continue
#         # dp[start] = [dist, routes, shortest, longest, calced?]
#         for v in voos[node]:
#             if depth + height > length:
#                 continue
#             if voos[node][v] + depth > dp[v][0]:
#                 continue
#             count, minl, maxl = dp[v][1:4]
#             if count > 0:
#                 dp[node][0] += count
#                 dp[node][0] %= mod
#                 dp[node][1] = min(dp[node][1], minl)
#                 dp[node][2] = max(dp[node][2], maxl)
#         dp[node][1] += 1
#         dp[node][2] += 1
#     return dp[0][0], dp[0][1], dp[0][2]

def route_count_iter(end, predecessor):
    # predecessor = [(p,False) for p in predecessor]
    length = distance_source[end]
    # visited = [False] * len(predecessor)
    added = [False] * len(predecessor)
    node = end
    dp[node] = [1,0,0]
    # stack = deque()
    # stack.append(node)
    queue = [node]
    added[node] = True
    while len(queue) > 0:
    # while len(stack) > 0:
        node = queue.pop(0)
        # node = stack.pop()
        # visited[node] = True
        for p in predecessor[node]:
            dp[p][0] += dp[node][0]
            dp[p][0] %= mod
            dp[p][1] = min(dp[p][1], dp[node][1]+1)
            dp[p][2] = max(dp[p][2], dp[node][2]+1)
            if not added[p]:
                queue.append(p)
                # stack.append(p)
                added[p] = True
    return dp[0][0], dp[0][1], dp[0][2]
    # for node in topological_sort:
    #     depth = distance_source[node]
    #     height = distance_target[node]
    #     start = node
    #     if node == end:
    #         dp[node] = [1,0,0]
    #         continue
    #     # dp[start] = [dist, routes, shortest, longest, calced?]
    #     for v in voos[node]:
    #         if depth + height > length:
    #             continue
    #         if voos[node][v] + depth > dp[v][0]:
    #             continue
    #         count, minl, maxl = dp[v][1:4]
    #         if count > 0:
    #             dp[node][0] += count
    #             dp[node][0] %= mod
    #             dp[node][1] = min(dp[node][1], minl)
    #             dp[node][2] = max(dp[node][2], maxl)
    #     dp[node][1] += 1
    #     dp[node][2] += 1
    # return dp[0][0], dp[0][1], dp[0][2]

if __name__ == "__main__":
    n,m = map(int, input().split())
    voos = {i: {} for i in range(n)}
    voos_inv = {i: {} for i in range(n)}
    # dp = [[distancia, shortest, longest] x n]
        
    for _ in range(m):
        a,b,w = map(int, input().split())
        if voos[a-1].get(b-1, INF) > w: 
            voos[a-1][b-1] = w
            voos_inv[b-1][a-1] = w
    
    top_sort = topological_sort(n, voos)
    distance_source, predecessor = dijkstra(n, voos, 0)
    distance_target, _ = dijkstra(n, voos_inv, n-1)
    price = distance_source[n-1]
    dp = [[0, INF, 0] for _ in distance_source]
    visited = [False] * n
    # routes, shortest, longest = route_count_iter(n-1, visited)
    routes, shortest, longest = route_count_iter(n-1, predecessor)
    print(price, routes, shortest, longest)
    
