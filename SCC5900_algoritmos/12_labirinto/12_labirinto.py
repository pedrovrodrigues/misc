if __name__ == "__main__":
    n = int(input())
    mod = 1000000007
    labirinto = []
    for i in range(n):
        labirinto.append(list(input()))
    dp = [[0 for i in range(n)] for j in range(n)]
    if labirinto[n-1][n-1] == '*' or labirinto[0][0] == '*':
        print(0)
        exit()

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if labirinto[i][j] == '*':
                dp[i][j] = 0
            elif i == n-1 and j == n-1:
                dp[i][j] = 1
            elif i == n-1:
                dp[i][j] = dp[i][j+1] % mod
            elif j == n-1:
                dp[i][j] = dp[i+1][j] % mod
            else:
                dp[i][j] = (dp[i+1][j] + dp[i][j+1]) % mod
    print(dp[0][0])