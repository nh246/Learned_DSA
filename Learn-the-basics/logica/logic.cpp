#include <bits/stdc++.h>
using namespace std;

void pattern6(int N)
{

    for (int i = 1; i <=N; i++)
    {

        for (int j=1; j<=N-j+1; j++)
        {
            cout <<j<<" ";
        }
       

        cout << endl;
    }
}

int main()
{   

    int N = 5;

    pattern6(N);

    return 0;
}