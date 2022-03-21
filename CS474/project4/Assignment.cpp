//
// Created by Adam on 12/7/2021.
//

#include "Assignment.h"

Assignment::Assignment(){dArr = new int[8];}
Assignment::~Assignment(){delete[] dArr;}

bool Assignment::parse(vector<string> words)
{
    if(words[1] == "?")
        return setIndex(words);
    else
    {
        setRegister(words);
        return false;
    }
}

bool Assignment::setIndex(vector<string> words)
{
    float* p;
    p = getRegister(words[0]);

    return *p != 0;
}

void Assignment::setRegister(vector<string> words)
{
    float* p1;
    p1 = getRegister(words[0]);

    *p1 = stof(words[2]);
}