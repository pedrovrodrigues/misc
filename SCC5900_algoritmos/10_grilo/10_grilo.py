INF = 10000

if __name__ == "__main__":
    n_index = int(input())
    indices = list(map(int, input().split()))
    leaps = [INF for i in range(n_index)]
    leaps[-1] = 0
    for i in range(n_index-2, -1, -1):
        leap = indices[i]
        if i + leap >= n_index:
            leaps[i] = 1
        else:
            min_leap = INF
            for j in range(1, leap+1):
                min_leap = min(min_leap, leaps[i+j])
            leaps[i] = min_leap + 1
    print(leaps[0] if leaps[0] < INF else "Salto impossivel")
        