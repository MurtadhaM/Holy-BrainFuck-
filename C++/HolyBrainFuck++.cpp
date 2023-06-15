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
#include <stdio.h>

using namespace std;

/**
 * This function reads the contents of a file and returns them as a string.
 * If the file cannot be read or the contents are malformed, the program exits.
 * @param filename - the name of the file to be read
 * @param program - the contents of the file
 * @return program - the contents of the file
 */
string readFile(std::string filename, std::string &program)
{
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
        if (program.length() > 2 && program.length() < 300)
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

/**
 * This function runs the Brainfuck program.
 * @param program - the Brainfuck code to be executed
 */
void runBrainfuck(std::string program)
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
            std::cin >> memory[pointer];
            break;
        case '[':
            if (memory[pointer] == 0)
            {
                int depth = 1;
                while (depth > 0)
                {
                    ip++;
                    if (program[ip] == '[')
                    {
                        depth++;
                    }
                    else if (program[ip] == ']')
                    {
                        depth--;
                    }
                }
            }
            break;
        case ']':
            if (memory[pointer] != 0)
            {
                int depth = 1;
                while (depth > 0)
                {
                    ip--;
                    if (program[ip] == ']')
                    {
                        depth++;
                    }
                    else if (program[ip] == '[')
                    {
                        depth--;
                    }
                }
            }
            break;
        }

        ip++;
    }
}

/**
 * This function gets interactive input from the user.
 * @return inputBuffer - the Brainfuck code entered by the user
 */
string get_interactive_input()
{
    string inputBuffer;
    std::cout << "Enter BrainFuck Code: ";
    cin >> inputBuffer;
    return inputBuffer;
}

#include <iostream>
#include <string>

#include <iostream>
#include <fstream>
#include <string>

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

/**
 * This is the main function of the program.
 * It reads the Brainfuck code from a file or from interactive input and runs it.
 * @param argc - the number of command line arguments
 * @param argv - an array of command line arguments
 * @return 0 if the program runs successfully, 1 otherwise
 */
int main(int argc, char *argv[])
{
    printBanner();

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
        program = get_interactive_input();

        runBrainfuck(program);
        return 0;
    }
    else
    {

        // Setting the filename
        std::string filename = argv[1];
        std::cout << "Reading filename passed in: " + filename << std::endl;
        try
        {

            program = readFile(filename, program);
            runBrainfuck(program);
        }
        catch (...)
        {
            std::cerr << "Error: filename not passed or not found" << std::endl;
            return 1;
        }
    }
    return 0;
}
