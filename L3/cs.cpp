#include<bits/stdc++.h>
using namespace std;
int main(){

    int N = 5e3;
    int nums[N];
    for (int i=0;i<N;++i)
        {
            nums[i] = rand();
            //cout<<nums[i]<<endl;
        }
    for (int i=0;i<N;++i)
    {
        cout<<nums[rand()%N]<<endl;
    }
    cout<<N;
}
