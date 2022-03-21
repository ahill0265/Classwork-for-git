//
// Created by Adam on 12/7/2021.
//

#include "Instruction.h"

Instruction::Instruction() = default;

Instruction::~Instruction() {};

void Instruction::printRegisters()
{
    cout << "w = " << w << " ";
    cout << "x = " << x << " ";
    cout << "y = " << y << " ";
    cout << "z = " << z << " ";
    cout << endl;
}

float* Instruction::getRegister(string line)
{
    float* p;

    switch(line[0])
    {
        case('w'):
            p = &w;
            break;
        case('x'):
            p = &x;
            break;
        case('y'):
            p = &y;
            break;
        case('z'):
            p = &z;
            break;
    }

    return p;
}

float Instruction::w;
float Instruction::x;
float Instruction::y;
float Instruction::z;


