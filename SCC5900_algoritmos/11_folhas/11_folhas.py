
if __name__ == "__main__":
    n_books, budget = map(int, input().split())
    prices = list(map(int, input().split()))
    pages = list(map(int, input().split()))

    dp = [[0 for _ in range(budget + 1)] for _ in range(n_books + 1)]
    for i in range(1, n_books + 1):
        for j in range(budget + 1):
            if prices[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - prices[i - 1]] + pages[i - 1])
    print(dp[n_books][budget])