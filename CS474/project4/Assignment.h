//
// Created by Adam on 12/7/2021.
//

#ifndef PROJECT4_ASSIGNMENT_H
#define PROJECT4_ASSIGNMENT_H

#include "Instruction.h"

class Assignment : public virtual Instruction
{
private:
    int* dArr;

public:
    Assignment();
    ~Assignment();

    bool parse(vector<string> words);
    void setRegister(vector<string> words);
    bool setIndex(vector<string> words);
};

#endif //PROJECT4_ASSIGNMENT_H
