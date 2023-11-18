// USER Input / Output

#include <bits/stdc++.h>

using namespace std;

int main()
{

    // Write your code here

    char ch;

    cin >> ch;

    if (isupper(ch))

        cout << 1;

    else if (islower(ch))

        cout << 0;

    else

        cout << -1;

    return 0;
}
// Data Types


int dataTypes(string type) {
	
	if (type=="Long"|| type =="Double")
	return 8;
	else if (type =="Character")
	return 1;
	else 
	return 4 ;
}

// If Else statements

string compareIfElse(int a, int b) {
	
    if(a>b){return "greater";}
    else if(a<b){return "smaller";}
    else if(a==b){return "equal";}
}

// Switch Statements

double areaSwitchCase(int ch, vector<double> a) {
	
		switch(ch) {
		case 1:
		return M_PI * pow(a[0], 2);
		case 2:
		return a[0] * a[1];
		default:
		return 0;
	}
}

// What are arrays, strings?

// For Loop

#include<bits/stdc++.h>
using namespace std;

int main()
{


        int n;
        cin >> n;
        int a = 0, b=1,s=0;
        for(int i=0; i<n; i++){
                s =a+b;
                a=b;
                b=s;
        }
        cout << a;


}

// While loops 
#include<iostream>
using namespace std;

int main() {
	// Write your code here
	int n;
cin >> n;
int odd = 0, even = 0;

while (n) {
    if (n % 2 == 0)
        even = even + n % 10;
    else
        odd = odd + n % 10;

    n = n / 10;
}

cout << even << " " << odd;

}

// functions 

#include <iostream>
using namespace std;
int Maximum(int x, int y)
{
	// Write your code here.
	if(x>=y)return x;
	else return y;
}
void Swap(int &x, int &y)
{
	int tem=x;
	x=y;
	y=tem;

}
int main()
{
	int test, a, b, r;
	cin >> test;
	cin >> a >> b;
	switch (test)
	{
	case 1:
		r = Maximum(a, b);
		cout << r;
		break;
	case 2:
		Swap(a, b);
		cout << a << " " << b;
		break;
	default:
		cout << "Invalid test option";
	}
	return 0;
}