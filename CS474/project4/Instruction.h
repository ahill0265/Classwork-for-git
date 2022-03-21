//
// Created by Adam on 12/7/2021.
//

#ifndef PROJECT4_INSTRUCTION_H
#define PROJECT4_INSTRUCTION_H

#include <iostream>
#include <vector>

using namespace std;

class Instruction
{
protected:
    static float w, x, y, z;
    Instruction();

public:
    virtual ~Instruction();

    void printRegisters();
    float* getRegister(string line);
    virtual bool parse(vector<string> words)=0;
};

#endif //PROJECT4_INSTRUCTION_H
