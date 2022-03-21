//
// Created by Adam on 12/7/2021.
//

#ifndef PROJECT4_CALCULATE_H
#define PROJECT4_CALCULATE_H

#include <cmath>

#include "Instruction.h"

class Calculate : virtual public Instruction
{
private:
    int* dArr;

public:
    Calculate();
    ~Calculate();

    bool parse(vector<string> words);
    void operations(float &x, const float& y, const float& z, string op);
    void operate(vector<string> words);
};

#endif //PROJECT4_CALCULATE_H
