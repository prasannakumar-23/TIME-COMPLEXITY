#include<iostream> 
using namespace std;

int fact(int n) 
{  
    if(n==0)
    return 1;
    else
    return fact(n-1) * n;
} 

void print_fun(char ch)
{
    int i=0,j;
    if(i==1)
  cout<<ch<<endl;
  else
  if(true)
  {
      for(j=1;  j<=5+3;j+=1)
      cout<<fact(j)<<endl;
  }
  
  else
  cout<<"Hi";
}

int main() 
{
    cout<<fact(5)<<endl; 
    print_fun('a');
    return 0;

}

