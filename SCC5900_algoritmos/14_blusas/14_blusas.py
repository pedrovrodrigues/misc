mod = 1000000007
global dp, n, m, shirts, full_mask, real_m
def solveDP(shirt, mask):
    if mask == full_mask:
        dp[shirt][mask] = 1
        return 1
    if shirt >= real_m:
        return 0
    if dp[shirt][mask] != -1:
        return dp[shirt][mask]    
    
    total = solveDP(shirt+1, mask)
    collection = shirts[shirt]
    for guest in collection:
        if ((1 << guest) & mask) == 0:
            total = (total + solveDP(shirt+1, mask|(1<<guest))) % mod
    dp[shirt][mask] = total
    return total


if __name__ == "__main__":
    n, m = map(int, input().split())
    guests = [[] for _ in range(n)] 
    shirts = [[] for _ in range(m+1)]
    all_shirts = []
    shirt_ids = {}
    for i in range(n):
        guest_shirts = list(map(int, input().split()))[1:]
        for gs in guest_shirts:
            if gs not in all_shirts:
                shirt_id = len(all_shirts)
                all_shirts.append(gs)
                shirt_ids[gs] = shirt_id
            else:
                shirt_id = shirt_ids[gs]
            shirts[shirt_id].append(i)
            guests[i].append(shirt_id)
    real_m = len(all_shirts)
    full_mask = (1 << n) - 1
    dp = [[-1] * (full_mask + 1) for _ in range(real_m+1)]
    
    possibilities = solveDP(0,0)
    print(possibilities)