from collections import deque
def BFS(v, visited, voos):
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in voos[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    while n != 0 and m != 0:
        relations = [{} for _ in range(n)]
        relations_inv = [{} for _ in range(n)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            relations[a-1][b-1] = 1
            relations_inv[b-1][a-1] = 1
            if c == 2:
                relations[b-1][a-1] = 1
                relations_inv[a-1][b-1] = 1
        
        visited = [False]*n
        BFS(0, visited, relations)
        if False in visited:
            print("0")
        else:
            visited = [False]*n
            BFS(0, visited, relations_inv)
            if False in visited:
                print("0")
            else:
                print("1")
        n, m = map(int, input().split())
