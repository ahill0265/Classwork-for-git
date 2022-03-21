#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

#include "Calculate.h"
#include "Assignment.h"

void runPC(int& index, const vector<string>& fileLines, Assignment assign, Calculate calc);

int main()
{
    cout << "Welcome to the C++ Programmable Calculator.\n";
    cout << "Make sure 'pc_input.txt' is in the program folder with the .exe.\n";
    cout << "r - Run all lines in the input file\n";
    cout << "s - Run one line of file input\n";
    cout << "x - Exit calculator\n";
    cout << "***************************************************************" << endl;

    //open file and put contents into a vector
    ifstream file;
    file.open("pc_input.txt");
    vector<string> fileLine;
    if(file.is_open())
    {
        string line;
        while(getline(file, line))
            fileLine.push_back(line);
        file.close();
    }
    else
    {
        cout << "File could not be opened";
        return 0;
    }

    char input;
    int fileIndex = 0;
    int counter = 0;
    Assignment assign = Assignment();
    Calculate calc = Calculate();
    while(true)
    {
        cout << "Input:";
        cin >> input;
        if(input == 'r')
        {
            while(fileIndex < fileLine.size())
            {
                if(counter == 100)
                {
                    cout << "Halting Instruction - 100 Executions reached" << endl;
                    counter = 0;
                    break;
                }
                else
                {
                    runPC(fileIndex, fileLine, assign, calc);
                    counter++;
                }
            }
        }
        else if(input == 's')
        {
            runPC(fileIndex, fileLine, assign, calc);
        }
        else if(input == 'x')
        {
            cout << "Exiting";
            break;
        }
        else
        {
            cout << "Invalid input" << endl;
        }
    }

    return 0;
}

void runPC(int& index, const vector<string>& fileLines, Assignment assign, Calculate calc)
{
    stringstream ss(fileLines[index]);
    string line;
    vector<string> words;
    while(getline(ss, line, ' '))
        words.push_back(line);

    cout << index << ": " << fileLines[index] << endl;

    if(words.size() == 3)
    {
        if(assign.parse(words))
        {
            index = stoi(words[2]) - 1;
            assign.printRegisters();
        }
        else
        {
            assign.printRegisters();
            index++;
        }
    }
    else
    {
         calc.parse(words);
         assign.printRegisters();
         index++;
    }

    if(index == fileLines.size())
        exit(0);
}
