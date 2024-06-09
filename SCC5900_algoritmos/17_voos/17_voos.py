INF = 10**9
if __name__ == "__main__":
    n, m = map(int, input().split())
    # distances = [n * [INF] for _ in range(n)]
    distances = {i: {} for i in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        distances[a-1][b-1] = 1
        distances[a-1][a-1] = 0
        distances[b-1][b-1] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i].get(j,INF) > distances[i].get(k,INF) + distances[k].get(j,INF):
                    distances[i][j] = distances[i].get(k,INF) + distances[k].get(j,INF)
    all_connected = True
    for i in range(n):
        for j in range(n):
            if distances[i].get(j,INF) == INF:
                all_connected = False
                break
    print("SIM" if all_connected else "NAO")
