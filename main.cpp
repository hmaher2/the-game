#include <iostream>
#include<math.h>

using namespace std;

int main()
{
    int tokens,y;
    int x=1;
    cout<<"enter tokens"<<endl;
    cin>>tokens;
    while ((tokens > 0) &&(tokens!=0))

    {

         cout<<"the number that u will subtract its square is y,enter it"<<endl;
      cin>>y;
          y=y*y;
            tokens=tokens-y;
            cout<<"the number of current tokens is "<<tokens<<endl;
            x=x++;


    }
    if (x%2==0){
        cout<<"player 1 wins!!";
    }
    else {
        cout<<"player 2 wins!!";
    }
    return 0;
}
