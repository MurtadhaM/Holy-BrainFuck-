/**
 * Author: Murtadha Marzouq
 * Description: hbf or (Holy Brain Fuck ) is a small project I created to help me learn more about programming languages
 * # Function: It takes in a brainfuck source code and interprets it in Rust like a. This maybe a front to all thing good and holy but it was fun. It is like cursing but in shaksprian style
 * # Resources:  https://www.youtube.com/watch?v=4uNM73pfJn0
 *
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdio.h>
using namespace std;

// FileReader interface for reading a file
class FileReader
{
public:
    virtual string readFile(string filename) = 0;
};

// BrainfuckInterpreter interface for interpreting a Brainfuck program
class BrainfuckInterpreter
{
public:
    virtual void runBrainfuck(string program) = 0;
};

// InteractiveInput interface for getting interactive input
class InteractiveInput
{
public:
    virtual string getInteractiveInput() = 0;
};

// HolyBrainFuck class that implements all three interfaces
class HolyBrainFuck : public FileReader, public BrainfuckInterpreter, public InteractiveInput
{
public:
    // Print Banner
    void printBanner()
    {
        std::ifstream bannerFile("./banner.txt");
        std::string banner;
        if (bannerFile.is_open())
        {
            while (getline(bannerFile, banner))
            {
                std::cout << banner << std::endl;
            }
            bannerFile.close();
        }
        else
        {
            std::cerr << "Error: Unable to open banner file" << std::endl;
        }
        std::cout << "Author: Murtadha Marzouq" << std::endl;
    }
    // Implementation of the FileReader interface
    string readFile(string filename) override
    {
        string program;
        try
        {
            std::ifstream file(filename);
            if (file.is_open())
            {
                std::string line;
                while (getline(file, line))
                {
                    program += line;
                }
                file.close();
            }

            // Check if the file contents are valid
            if (program.length() > 2 )
            {
                return program;
            }
            else
            {
                std::cout << "File Content is malformed or incorrect exiting ..." << endl;
                 
                std::exit(1);
            }
            return program;
        }
        catch (...)
        {
            std::cerr << "File read error! exiting ..." << endl;
            std::exit(1);
        }
    }

    // Implementation of the BrainfuckInterpreter interface
    void runBrainfuck(string program) override
    {
        std::vector<int> memory(1, 0);
        int pointer = 0;

        size_t ip = 0;
        char instruction;
        while (ip < program.size())
        {
            instruction = program[ip];

            switch (instruction)
            {
            case '>':
                pointer++;
                if (pointer == memory.size())
                {
                    memory.push_back(0);
                }
                break;
            case '<':
                pointer--;
                if (pointer < 0)
                {
                    std::cerr << "Error: pointer out of bounds" << std::endl;
                    return;
                }
                break;
            case '+':
                memory[pointer]++;
                break;
            case '-':
                memory[pointer]--;
                break;
            case '.':
                std::cout << static_cast<char>(memory[pointer]);
                break;

            case ',':

                memory[pointer] = getInteractiveInput()[0];
                break;
            case '[':
                if (memory[pointer] == 0)
                {
                    int loop = 1;
                    while (loop > 0)
                    {
                        instruction = program[++ip];
                        if (instruction == '[')
                        {
                            loop++;
                        }
                        else if (instruction == ']')
                        {
                            loop--;
                        }
                    }
                }
                break;
            case ']':

                if (memory[pointer] != 0)
                {
                    int loop = 1;
                    while (loop > 0)
                    {
                        instruction = program[--ip];
                        if (instruction == '[')
                        {
                            loop--;
                        }
                        else if (instruction == ']')
                        {
                            loop++;
                        }
                    }
                }
                break;
            default:

                break;
            }
            ip++;
        }
    }

    // Implementation of the InteractiveInput interface
    string getInteractiveInput() override
    {
        string input;
        std::cin >> input;
        return input;
    }
};

// Main function that uses the HolyBrainFuck class to read and execute a Brainfuck program
int main(int argc, char *argv[])
{
    HolyBrainFuck interpreter;
    interpreter.printBanner();

    // Declare variables
    std::string program; // THE BrainFuck Code
    std::string output;  // Output to STDOUT

    if (argc != 2)
    {
        std::cerr << "Usage: " << argv[0] << " <filename> || -i <start interactive>" << std::endl;

        return 1;
    }
    else if (string(argv[1]) == "-i")
    {
        program = interpreter.getInteractiveInput();

        interpreter.runBrainfuck(program);
        return 0;
    }

    else
    {

        // Setting the filename
        std::string filename = argv[1];

        try
        {
            program = interpreter.readFile(filename);
            interpreter.runBrainfuck(program);
        }
        catch (...)
        {
            std::cerr << "Error: filename not passed or not found" << std::endl;
            return 1;
        }
    };
    return 0;
};
