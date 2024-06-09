#include <iostream>
#include <vector>
#include <queue>
#include <climits>

typedef long long ll;
const ll INF = LLONG_MAX - 10;

using namespace std;

vector<int> BFS_path(vector<vector<ll>>& graph, int source, int sink, ll& bottleneck) {
    int n = graph.size();
    vector<bool> visited(n, false);
    vector<int> parent(n, -1);
    queue<int> q;
    q.push(source);
    visited[source] = true;

    while (!q.empty() && !visited[sink]) {
        int u = q.front();
        q.pop();
        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] > 0) {
                visited[v] = true;
                parent[v] = u;
                q.push(v);
            }
        }
    }

    if (!visited[sink]) {
        return vector<int>();
    }

    vector<int> path;
    int v = sink;
    bottleneck = INF;
    while (v != source) {
        path.push_back(v);
        bottleneck = min(bottleneck, graph[parent[v]][v]);
        v = parent[v];
    }
    path.push_back(source);
    return path;
}

ll edmonds_karp(vector<vector<ll>>& capacities, int source, int sink) {
    int n = capacities.size();
    vector<vector<ll>> residual(n, vector<ll>(n, 0));
    for (int u = 0; u < n; u++) {
        for (int v = 0; v < n; v++) {
            residual[u][v] = capacities[u][v];
        }
    }
    ll max_flow = 0;

    while (true) {
        ll bottleneck = INF;
        vector<int> path = BFS_path(residual, source, sink, bottleneck);
        if (path.empty()) {
            break;
        }
        for (int i = 0; i < path.size() - 1; i++) {
            int u = path[i+1];
            int v = path[i];
            bottleneck = min(bottleneck, residual[u][v]);
        }
        max_flow += bottleneck;
        for (int i = 0; i < path.size() - 1; i++) {
            int u = path[i+1];
            int v = path[i];
            residual[u][v] -= bottleneck;
            residual[v][u] += bottleneck;
        }
    }
    return max_flow;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<ll>> capacities(n, vector<ll>(n, 0));
    for (int i = 0; i < m; i++) {
        int a, b;
        ll c;
        cin >> a >> b >> c;
        a--; b--;
        capacities[a][b] += c;
    }
    cout << (n > 1 ? edmonds_karp(capacities, 0, n - 1) : 0) << endl;
    return 0;
}
// from collections import deque
// INF = 10**10
// def BFS_path(graph, source, sink): 
//     visited = [False] * len(graph)
//     parent = [-1] * len(graph)
//     queue = deque()
//     queue.append(source)
//     visited[source] = True
//     while queue and not visited[sink]:
//         u = queue.popleft()
//         for v in graph[u]:
//             if not visited[v] and graph[u][v] > 0:
//                 visited[v] = True
//                 parent[v] = u
//                 queue.append(v)
//     if not visited[sink]:
//         return None, 0
//     path = []
//     v = sink
//     bottleneck = INF
//     while v != source:
//         path.append(v)
//         bottleneck = min(bottleneck, graph[parent[v]][v])
//         v = parent[v]
//     path.append(source)
//     path.reverse()
//     return path, bottleneck

// def edmonds_karp(capacities, source, sink):
//     n = len(capacities)
//     residual = [{
// v: capacities[u][v] for v in capacities[u]} for u in range(n)]
//     max_flow = 0

//     while True:
//         path, bottleneck = BFS_path(residual, source, sink)
//         if path is None:
//             break
//         max_flow += bottleneck
//         for i in range(len(path)-1):
//             u, v = path[i], path[i+1]
//             residual[u][v] = residual[u].get(v, 0) - bottleneck
//             residual[v][u] = residual[v].get(u, 0) + bottleneck
//     return max_flow


// if __name__ == "__main__":
//     n, m = map(int, input().split())
//     capacities = [{} for _ in range(n)]
//     for _ in range(m):
//         a, b, c = map(int, input().split())
//         capacities[a-1][b-1] = capacities[a-1].get(b-1, 0) + c
//     print(edmonds_karp(capacities, 0, n-1) if n > 1 else 0)