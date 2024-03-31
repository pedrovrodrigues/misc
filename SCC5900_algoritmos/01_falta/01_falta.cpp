#include <stdio.h>
#include <vector>

int main()
{
    long unsigned int size, num;
    scanf("%lu", &size);
    std::vector<bool> number_check(size, false);
    for(long unsigned int i=1; i<size; ++i){
        scanf("%lu", &num);
        if(num>0)
            number_check[num-1] = true;
    }
    for(long unsigned int i=0; i<size; ++i) {
        if(!number_check[i]){
            printf("%lu\n", i+1);
            break;
        }
    }
    return 0;
}
