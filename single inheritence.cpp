#include<iostream>
using namespace std;
class A
{
protected:
int a,b;
public:
void get()
{
cout<<"Enter any two integer values";
cin>>a>>b;
}
};
class B:public A
{
int c;
public:
void add()
{
c=a+b;
cout<<a<<"+"<<b<<"="<<c;
}
};
int main()
{
B b;
b.get();
b.add();
} 

