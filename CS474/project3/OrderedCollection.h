//
// Created by Adam on 11/14/2021.
//

#ifndef PROJECT3_ORDEREDCOLLECTION_H
#define PROJECT3_ORDEREDCOLLECTION_H

#include <iostream>

using namespace std;

class OrderedCollection
{
    private:
    //instance variables
        int first, last;
        int _size, _basicSize;
        int* dynamicArray;
    //assisting methods
        void grow();
        void shiftLeft(int i,int flag);
        void shiftRight(int i,int flag);

    public:
    //constructors
        OrderedCollection();
        OrderedCollection(const OrderedCollection& oc1);
        OrderedCollection(int i);
        ~OrderedCollection();
    //methods
        bool isEmpty();
        int size();
        int basicSize();
        int& operator[](int i);
        OrderedCollection& insertAt(int i, int x);
        int find(int x);
        OrderedCollection& removeAt(int i);
        OrderedCollection& iterate(int (*fn)(int));
        OrderedCollection& operator=(const OrderedCollection&);
    //testing purposes
        void printArrayTest();
        void testInfo();

};

#endif //PROJECT3_ORDEREDCOLLECTION_H
