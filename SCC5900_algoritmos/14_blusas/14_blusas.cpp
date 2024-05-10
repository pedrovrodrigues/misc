#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int mod = 1000000007;
vector<vector<int>> dp;
int n, m, real_m, full_mask;
vector<vector<int>> shirts;

int solveDP(int shirt, int mask) {
    if (mask == full_mask) {
        dp[shirt][mask] = 1;
        return 1;
    }
    if (shirt >= real_m) {
        return 0;
    }
    if (dp[shirt][mask] != -1) {
        return dp[shirt][mask];
    }

    int total = solveDP(shirt + 1, mask);
    vector<int> collection = shirts[shirt];
    for (int guest : collection) {
        if (((1 << guest) & mask) == 0) {
            total = (total + solveDP(shirt + 1, mask | (1 << guest))) % mod;
        }
    }
    dp[shirt][mask] = total;
    return total;
}

int main() {
    cin >> n >> m;

    vector<vector<int>> guests(n);
    shirts.resize(m + 1);
    vector<int> all_shirts;
    vector<int> shirt_ids(m + 1);
    for (int i = 0; i < n; i++) {
        int num_shirts;
        cin >> num_shirts;
        for (int j = 0; j < num_shirts; j++) {
            int gs, shirt_id;
            cin >> gs;
            if (all_shirts.empty() ||
                std::find(all_shirts.begin(), all_shirts.end(), gs) == all_shirts.end()) { // Use std::find with the correct arguments
                all_shirts.push_back(gs);
                shirt_id = all_shirts.size() - 1;
                shirt_ids[gs] = shirt_id;
            } else {
                shirt_id = shirt_ids[gs];
            }
            shirts[shirt_id].push_back(i);
            guests[i].push_back(shirt_id);
        }
    }
    real_m = all_shirts.size();
    full_mask = (1 << n) - 1;
    dp.resize(real_m + 1, vector<int>(full_mask + 1, -1));


    int possibilities = solveDP(0, 0);
    cout << possibilities << endl;

    return 0;
}
