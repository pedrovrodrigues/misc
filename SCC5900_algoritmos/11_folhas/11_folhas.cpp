#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n_books, budget;
    cin >> n_books >> budget;

    vector<int> prices(n_books);
    for (int i = 0; i < n_books; i++) {
        cin >> prices[i];
    }

    vector<int> pages(n_books);
    for (int i = 0; i < n_books; i++) {
        cin >> pages[i];
    }

    vector<vector<int>> dp(n_books + 1, vector<int>(budget + 1, 0));
    for (int i = 1; i <= n_books; i++) {
        for (int j = 0; j <= budget; j++) {
            if (prices[i - 1] > j) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - prices[i - 1]] + pages[i - 1]);
            }
        }
    }

    cout << dp[n_books][budget] << endl;

    return 0;
}
