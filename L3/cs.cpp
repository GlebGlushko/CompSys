#include<bits/stdc++.h>
using namespace std;
int main(){

    clock_t Start = clock();
    int N = 5e5;
    int nums[N];
    for (int i=0;i<N;++i)
        {
            nums[i] = rand();
            //cout<<nums[i]<<endl;
        }
    for (int e =0; e<100;++e)
    for (int i=0;i<N;++i)
    {
        int x = nums[rand()%N];
    }

    printf("Time taken: %.2fs\n", (double)(clock() - Start)/CLOCKS_PER_SEC);

}
