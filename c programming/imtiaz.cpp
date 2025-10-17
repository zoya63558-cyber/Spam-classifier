#include<iostream>
using namespace std;

class Rectangle { 
int l,b;
public:Rectangle(int x , int y)
{ 
    l=x; b=y;
}
int area()
{ 
    return l*b;
}
};

void display(Rectangle &s)
{
    cout<< s.area();
}

int main ()
{
    Rectangle r(10,20);
    display(r);
    return 0;
}
