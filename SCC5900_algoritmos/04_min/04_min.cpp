#include <stdio.h>
#include <bits/stdc++.h> 

using namespace std;

int main()
{
    int height, month, count=0;
    vector<int> monthlyGrowth;
    
    scanf("%d", &height);
    for(int i=0; i<12; ++i){
        scanf("%d", &month);
        monthlyGrowth.push_back(month);
    }
    monthlyGrowth.push_back(0);
    sort(monthlyGrowth.begin(), monthlyGrowth.end(), greater<int>());
    for(int i=0; i<=12; ++i){
        if(count >= height){
            printf("%d\n", i);
            return 0;
        }
        count += monthlyGrowth[i];
    }
    printf("-1\n");
    return 0;
}
/*
5
1 1 1 1 2 2 3 2 2 1 1 1
*/