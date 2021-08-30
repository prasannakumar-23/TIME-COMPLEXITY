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
    int i=0;
    if(i==1)
  cout<<ch<<endl;
  else
  if(true)
  {
      for(int j=1;j<=5;j++)
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

