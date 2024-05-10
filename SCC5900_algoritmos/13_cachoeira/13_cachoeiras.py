INF = 1e9
global full_mask, memo, graph

def tsp(mask, pos):
    if mask == full_mask:
        return 0
    if memo[mask][pos] != -1:
        return memo[mask][pos]
    ans = INF
    for i in range(n):
        if mask & (1 << i) == 0:
            ans = min(ans, graph[pos][i] + tsp(mask | (1 << i), i))
    memo[mask][pos] = ans
    return ans

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a-1][b-1] = d
        graph[b-1][a-1] = d
    for i in range(n):
        graph[i][i] = 0
    
    full_mask = (1 << n) - 1
    memo = [[-1 for _ in range(n)] for _ in range(1 << n)]
    for i in range(n):
        memo[full_mask][i] = 0
    print(tsp(1, 0))