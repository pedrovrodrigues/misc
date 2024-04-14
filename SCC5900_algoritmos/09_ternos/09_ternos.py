INF = 10**10

if __name__ == "__main__":
    n_ternos = int(input())
    ternos = list(map(int, input().split()))
    terno_cost = [-1 for i in range(n_ternos)]
    
    terno_cost[-1] = 0
    for i in range(n_ternos-2, -1, -1):
        cost1 = abs(ternos[i] - ternos[i+1]) + terno_cost[i+1] if i+1 < n_ternos else INF
        cost2 = abs(ternos[i] - ternos[i+2]) + terno_cost[i+2] if i+2 < n_ternos else INF
        terno_cost[i] = min(cost1, cost2)
    print(terno_cost[0])