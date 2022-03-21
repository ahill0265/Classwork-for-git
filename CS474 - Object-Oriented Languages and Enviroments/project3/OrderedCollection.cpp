//
// Created by Adam on 11/14/2021.
//

// Everything except insert and remove as a version to turn in before taking a nap.
// It only took 2 days to realize how this collection works. And they say only smart people are in this major.

#include "OrderedCollection.h"

//default constructor
OrderedCollection::OrderedCollection()
{
    first = 4;
    last = 3;
    _size = 0;
    _basicSize = 8;
    dynamicArray = new int [_basicSize];
}

//copy constructor
OrderedCollection::OrderedCollection(const OrderedCollection &oc)
{
    first = oc.first;
    last = oc.last;
    _size = oc._size;
    _basicSize = oc._basicSize;
    dynamicArray = new int [_basicSize];

    for(int i = 0; i < _basicSize; i++)
        dynamicArray[i] = oc.dynamicArray[i];
}

//argument constructor
OrderedCollection::OrderedCollection(int i)
{
    first = 4;
    last = 4;
    _size = 1;
    _basicSize = 8;
    dynamicArray = new int [_basicSize];

    dynamicArray[first] = i;
}

//destructor
OrderedCollection::~OrderedCollection()
{
    delete[] dynamicArray;
    dynamicArray = nullptr;
    _size = 0;
    _basicSize = 0;
}

/* bool isEmpty()
 * returns a boolean for if the ordered collection is empty
 */
bool OrderedCollection::isEmpty()
{
    return (_size == 0);
}

/* int size()
 * returns the current size (number of elements currently stored in the collection)
 */
int OrderedCollection::size()
{
    return _size;
}

/* int basicSize()
 * returns the current size of the underlying array (how many blocks of memory are allocated)
 */
int OrderedCollection::basicSize()
{
    return _basicSize;
}

/* indexing operator overload
 * returns a pointer to the index of the underlying array that corresponds to the input index of the ordered collection
 * throws and out of range error if you try to access a spot out of range of the collection
 */
int& OrderedCollection::operator[](int i)
{
    if(i < 0 || i > (last-first))
        __throw_out_of_range("Error: Out of bounds of ordered collection instance");

    return dynamicArray[first+i];
}

/* OrderedCollection& insertAt(int i, int x)
 * inserts element x at index i of the ordered collection
 * grows the underlying array if full
 * returns the modified receiver
 */
OrderedCollection& OrderedCollection::insertAt(int i, int x)
{
    int flag = 0; //shift out

    if(_size == _basicSize) //inserting into a full collection
        grow();

    if(i == 0) //inserting into start of collection...
        if(isEmpty()) //...and it's empty
            last++;
        else if(first != 0) //...and there is space on the left side of the array
            first--;
        else //..and there is no space on the left side of the array, but there is space on the right side
            shiftRight(i, flag);
    else if(i == (last-first+1)) //inserting into end of collection...
        if(last != (_basicSize-1)) //...and there's space on the right side of the array
            last++;
        else //..and there's no space on the right side of the array, but there is space on the left side
            shiftLeft(i, flag);
    else
        if(first != 0) //check for space on the left first
            shiftLeft(i, flag);
        else //otherwise use space on the right
            shiftRight(i, flag);

    (*this)[i] = x;
    _size++;

    return *this;
}

/* int find(int x)
 * returns the index of the first time element x is found in the ordered collection
 */
int OrderedCollection::find(int x)
{
    for (int i = 0; i < (last-first+1); i++)
    {
        if ((*this)[i] == x)
            return i;
    }
    return -1;
}

/* OrderedCollection& removeAt(int i)
 * removes the element at index i of the ordered collection
 * shifts elements on either side in after deletion
 * returns modified receiver
 */
OrderedCollection& OrderedCollection::removeAt(int i)
{
    int flag = 1; //shift in

    if(i < 0 || i > (last-first)) //do nothing if i is out of bounds
        return *this;

    if(i == 0) //if i is the first element...
        if(size() == 1) //and the only element, then set first and last to signifiers for an empty collection
        {
            first = 4;
            last = 3;
        } else //move first up so the previous first can not be reached
            first++;
    else if(i == (last-first+1)) //if i is the last element...
        last--; //then shift last back so collection ends the element before the old last
    else //i is an element somewhere between
        if(i < size()/2)  //i is in the first half, shift elements to the left of it in
            shiftRight(i,flag);
        else //otherwise shift elements on the right side in
            shiftLeft(i, flag);

    _size--;
    return *this;
}

/* OrderedCollection& iterate(int (*fn)(int))
 * applies an input function on every element in the ordered collection
 * returns modified reciever
 */
OrderedCollection& OrderedCollection::iterate(int (*fn)(int))
{
    for(int i = first; i < last+1; i++)
        dynamicArray[i] = (*fn)(dynamicArray[i]);

    return *this;
}

//assignment operator
OrderedCollection& OrderedCollection::operator=(const OrderedCollection &oc)
{
   if(this == &oc)
       return *this;

    first = oc.first;
    last = oc.last;
    _size = oc._size;
    _basicSize = oc._basicSize;

    delete[] dynamicArray;
    dynamicArray = new int [_basicSize];

    for(int i = 0; i < _basicSize; i++)
        dynamicArray[i] = oc.dynamicArray[i];

    return *this;

}

/* void grow()
 * doubles size of the underlying array
 */
void OrderedCollection::grow()
{
    _basicSize = _basicSize * 2;

    int* tempArray = new int [_basicSize];

    for(int i = 0; i < _size; i++)
        tempArray[i] = dynamicArray[i];

    delete[] dynamicArray;

    dynamicArray = tempArray;
}

/* void shiftLeft(int i, int flag)
 * shifts elements on a certain side of i to the left
 * if flag = 0, elements on the left side are shifted
 * if flag = 1, elements on the right side are shifted
 * insert uses 0, removal uses 1
 */
void OrderedCollection::shiftLeft(int i, int flag)
{
    if(flag == 0) //shifting everything on the left side of the element towards 0
    {
        --first;
        for (int j = 0; j < i; j++)
            (*this)[j] = (*this)[j + 1];
    }
    else //shifting everything on the right side of the element towards _basicSize;
    {
        for(int j = i; j < last; j++)
            (*this)[j] = (*this)[j + 1];
        last--;
    }
}

/* void shiftRight(int i, int flag)
 * shifts elements on a certain side of i to the right
 * if flag = 0, elements on the right are shifted
 * if flag = 1, elements on the left are shifted
 * insert uses 0, removal uses 1
 */
void OrderedCollection::shiftRight(int i, int flag)
{
    if(flag == 0) //shifting right side out
    {
        last++;
        for (int j = _size; j > i; j--)
            (*this)[j] = (*this)[j - 1];
    }
    else //shifted left side in
    {
        for (int j = i; j > first; j--)
            (*this)[j] = (*this)[j - 1];
        first++;
    }
}

/* void printArrayTest()
 * testing method that prints out contents of the collection
 */
void OrderedCollection::printArrayTest()
{
    for(int i = 0; i < this->size(); i++)
        cout << (*this)[i] << ' ';

    cout << endl;
}

/* void testInfo()
 * testing method that prints out contents of instance variables
 */
void OrderedCollection::testInfo()
{
    cout << "Size= " << size() << endl;
    cout << "Total size= " << basicSize() << endl;
    cout << "First= " << first << " Last= " << last << endl;
    for(int i = 0; i < _basicSize; i++)
        cout << dynamicArray[i] << ' ';
    cout << endl;
}
