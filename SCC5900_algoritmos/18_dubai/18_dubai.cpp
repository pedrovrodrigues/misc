#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <chrono>

using namespace std;
typedef long long ll;

const ll mod = 1e9 + 7;
const double INF = 1e15;

class Node {
    public:
        int v;
        double distance;

        Node();
        Node(int v, double distance);

        bool operator<(const Node& other) const {
            return this->distance > other.distance;
        }
};

Node::Node() {
    this->v = -1;
    this->distance = INF;
}

Node::Node(int v, double distance) {
    this->v = v;
    this->distance = distance;
}

vector<vector<ll>> dp;
vector<double> distances;
unordered_map<int, unordered_map<int, int>> voos;

vector<double> dijkstra(int V, unordered_map<int, unordered_map<int, int>>& adj, int S) {
    vector<bool> visited(V, false);
    unordered_map<int, Node> map;
    priority_queue<Node> q;

    map[S] = Node(S, 0);
    q.push(Node(S, 0));
    double target_distance = INF;

    while (!q.empty()) {
        Node n = q.top();
        q.pop();
        int v = n.v;
        double distance = n.distance;
        visited[v] = true;

        for (auto& i_w : adj[v]) {
            int i = i_w.first;
            int w = i_w.second;
            if (!visited[i]) {
                if (map.find(i) == map.end()) {
                    map[i] = Node(v, distance + w);
                } else {
                    Node& sn = map[i];
                    if (distance + w < sn.distance) {
                        sn.v = v;
                        sn.distance = distance + w;
                    }
                }
                q.push(Node(i, distance + w));
            }
        }
    }

    vector<double> result(V, INF);
    for (int i = 0; i < V; i++) {
        if (map.find(i) != map.end()) {
            result[i] = map[i].distance;
        }
    }

    return result;
}

vector<int> topological_ordering(unordered_map<int, unordered_map<int, int>>& adj) {
    vector<int> result;
    vector<bool> visited(adj.size(), false);
    stack<int> st;
    st.push(0);
    visited[0] = true;

    while (!st.empty()) {
        int v = st.top();
        st.pop();
        if (!visited[i]) {
            visited[i] = true;
        }
    
    
        for (auto& i_w : adj[v]) {
            int i = i_w.first;
            if (!visited[i]) {
                visited[i] = true;
            }
        }
        result.push_back(v);
    }

    return result;
}


tuple<ll, ll, ll> route_count_iter(int end) {
    // vector<pair<int, ll>> nodes_by_depth;
    // for (int i = 0; i < dp.size(); i++) {
    //     nodes_by_depth.push_back({i, dp[i][0]});
    // }
    // sort(nodes_by_depth.rbegin(), nodes_by_depth.rend());
    vector<int> nodes_by_depth = topological_ordering(voos);
    for(int i = 0; i < nodes_by_depth.size(); i++) {
        int node = nodes_by_depth[i];
        int start = node;
        double depth = distances[node];
        if (node == end) {
            dp[node][0] = 1;
            dp[node][1] = 0;
            dp[node][2] = 0;
            continue;
        }
        for (auto& v_w : voos[node]) {
            int v = v_w.first;
            int w = v_w.second;
            if (w + depth > distances[v]) {
                continue;
            }
            ll count = dp[v][0];
            ll minl = dp[v][1];
            ll maxl = dp[v][2];
            if (count > 0) {
                dp[node][0] += count;
                dp[node][0] %= mod;
                dp[node][1] = min(dp[node][1], minl + 1);
                dp[node][2] = max(dp[node][2], maxl + 1);
            }
        }
    }
    return {dp[0][0], dp[0][1], dp[0][2]};
}

int main() {
    int n, m;
    ifstream myFile ("18_dubai.ini", ios::in);
    myFile >> n >> m;
    voos = unordered_map<int, unordered_map<int, int>>(n);

    cout << "n = " << n << ", m = " << m << endl;
    chrono::steady_clock::time_point begin = chrono::steady_clock::now();
    for (int i = 0; i < m; i++) {
        int a, b, w;
        myFile >> a >> b >> w;
        a--; b--;
        if (voos[a].find(b) == voos[a].end() || voos[a][b] > w) {
            voos[a][b] = w;
        }
    }
    chrono::steady_clock::time_point end = chrono::steady_clock::now();
    cout << "Read time = " << chrono::duration_cast<chrono::microseconds>(end - begin).count() << "[µs]" << endl;

    begin = chrono::steady_clock::now();

    distances = dijkstra(n, voos, 0);

    end = chrono::steady_clock::now();
    cout << "Djikstra time = " << chrono::duration_cast<chrono::microseconds>(end - begin).count() << "[µs]" << endl;
    double price = distances[n - 1];
    dp = vector<vector<ll>>(n, vector<ll>(3, 0));
    for (int i = 0; i < n; i++) {
        dp[i][1] = INF;
    }
    ll routes, shortest, longest;
    
    begin = chrono::steady_clock::now();
    tie(routes, shortest, longest) = route_count_iter(n - 1);
    end = chrono::steady_clock::now();
    cout << "Routes time = " << chrono::duration_cast<chrono::microseconds>(end - begin).count() << "[µs]" << endl;

    cout << (ll) price << " " << routes << " " << shortest << " " << longest << endl;

    return 0;
}