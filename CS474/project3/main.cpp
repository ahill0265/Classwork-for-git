#include <iostream>
#include "OrderedCollection.h"

int foo(int x){return x+2;}

int main() {
    OrderedCollection dArr;
//    OrderedCollection dArr2(2);
//    OrderedCollection dArr3(dArr2);

    for(int i = 0; i < 16; i++)
        dArr.insertAt(i,i);

    dArr.removeAt(6);
    dArr.insertAt(3,42);


    dArr.testInfo();
    dArr.printArrayTest();
}