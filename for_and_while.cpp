#include <bits/stdc++.h>
using namespace std;
void he(int n)
{
	int j;
	for(j=1;j<=n;j=j*2)
	cout<<"Hello ";
}
void hello(int n)
{
	int i;
	for(i=1;i<=n;i++)
	he(n);
}

int main() {
    int i,j,k,l;
	int n=10;
	for(i=1;i<=n;i++)
	cout<<i<<endl;

	
	for(i=1;i<=n;i+=1)
	{
		for(j=1;j<=n;j=j+2)
		{
			for(k=1;k<=10;k++)
			{
				for(l=n;l>=1;l--)
				hello(n);
			}
		}
	}

	// i=1;
	// while(i<=10){
	//     cout<<i;
	//     i++;
	// }
	return 0;
}