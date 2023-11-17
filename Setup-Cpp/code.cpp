#include<iostream>

#include<bits/stdc++.h>

using namespace std;

 

int main() {

    // Write your code here

    char ch;

    cin>>ch;

 

    if (isupper(ch))

        cout<<1;

    else if(islower(ch))

        cout<<0;

    else

        cout<<-1;

    

    return 0;   

}