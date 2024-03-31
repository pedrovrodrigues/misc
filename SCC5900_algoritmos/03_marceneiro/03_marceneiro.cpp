#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

typedef pair<pair<int, int>, int> orderItem;
struct comparator
{
    bool operator()(orderItem left, orderItem right){
        // true <=> left comes first
        // conditions: left (fine/time) > right (fine/time) <=> left.fine*right.time > right.fine*left.time
        // tie break: left.j < right.j
        int fineTimeDiff = left.first.first*right.first.second - right.first.first*left.first.second;
        return (fineTimeDiff > 0) || ((fineTimeDiff == 0) && left.second > right.second);
    }
};

int main()
{
    int nTestCase, nOrders, time, fine;
    priority_queue<orderItem, vector<orderItem>, comparator> pq;
    orderItem order;
    
    scanf("%d", &nTestCase);
    for(int i=0; i<nTestCase; ++i){
        scanf("%d", &nOrders);
        for(int j=0; j<nOrders; ++j) {
            scanf("%d %d", &time, &fine);
            order = make_pair(make_pair(time, fine), j);
            pq.push(order);
        }
        if(i>0){
            printf("\n");
        }
        for(int j=0; j<nOrders; ++j) {
            order = pq.top();
            if(j>0)
                printf(" ");
            printf("%d", order.second+1);
            pq.pop();
        }
        printf("\n");
    }
    return 0;
}
