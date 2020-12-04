
#include<iostream.h>
#include<conio.h>
class student
{
protected:
int rno,m1,m2;
public:
void get()
{
cout<<"Enter the Roll no :";
cin>>rno;
cout<<"Enter the two marks :";
cin>>m1>>m2;
}
};
class sports
{
protected:
intsm; // sm = Sports mark
public:
voidgetsm()
{
cout<<"\nEnter the sports mark :";
cin>>sm;
}
};
classstatement:publicstudent,public sports
{
Int tot,avg;
public:
void display()
{
tot=(m1+m2+sm);
avg=tot/3;
cout<<"\n\n\tRoll No : "<<rno<<"\n\tTotal : "<<tot;
cout<<"\n\tAverage : "<<avg;
}
};
void main()
{
clrscr();
statementobj;
obj.get();
obj.getsm();
obj.display();
getch();
} 
