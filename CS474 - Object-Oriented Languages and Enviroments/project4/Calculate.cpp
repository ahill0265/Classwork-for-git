//
// Created by Adam on 12/7/2021.
//

#include "Calculate.h"

Calculate::Calculate()
{
    dArr = new int[8];
}

Calculate::~Calculate()
{
    delete[] dArr;
}

bool Calculate::parse(vector<string> words)
{
    operate(words);
    return true;
}

void Calculate::operations(float &x, const float& y, const float& z, string op)
{
    switch(op[0])
    {
        case '+':
            x = y + z;
            break;
        case '-':
            x = y - z;
            break;
        case '*':
        {
            int opSize = op.size();
            if (opSize == 2)
                x = pow(y, z);
            else
                x = y * z;
        }
        break;
        case '/':
            x = y / z;
            break;
    }
}

void Calculate::operate(vector<string> words)
{
    float* p1;
    float* p2;
    p1 = getRegister(words[0]);
    p2 = getRegister(words[2]);

    if(isdigit((words[4][0])))
    {
        float constant = stof(words[4]);
        operations(*p1, *p2, constant, words[3]);
    } else
    {
        float* p3;
        p3 = getRegister(words[4]);
        operations(*p1, *p2, *p3, words[3]);
    }

}






