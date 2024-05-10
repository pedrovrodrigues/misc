mod = 1000000007
global dp, n, m, shirts, full_mask
def solveDP(shirt, mask):
    if mask == full_mask:
        return 1
    if shirt > m:
        return 0
    if dp[shirt, mask] != -1:
        return dp[shirt, mask]    
    
    total = solveDP(shirt+1, mask)
    collection = shirts[shirt]
    for guest in collection:
        if ((1 << guest) & mask) == 0:
            total = (total + solveDP(shirt+1, mask|(1<<guest))) % mod
    dp[shirt, mask] = total
    return total


if __name__ == "__main__":
    n, m = map(int, input().split())
    guests = [[] for _ in range(n)] 
    shirts = [[] for _ in range(m+1)]
    for i in range(n):
        guest_shirts = list(map(int, input().split()))[1:]
        for gs in guest_shirts:
            shirts[gs].append(i)
            guests[i].append(gs)
    full_mask = (1 << n) - 1
    dp = ([-1] * (full_mask + 1)) * (m+1)
    
    possibilities = solveDP(1,0)
    print(possibilities)