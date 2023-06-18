use std::io;
use std::io::Read;

use crate::lexer;
use crate::parser;
use crate::Instruction;

pub fn run(instructions: &Vec<Instruction>, tape: &mut Vec<u8>, data_pointer: &mut usize) {
    // Iterate over the instructions
    for instr in instructions {
        // Execute the instruction
        match instr {
            Instruction::IncrementPointer => {
                *data_pointer += 1;
            }
            Instruction::DecrementPointer => {
                *data_pointer -= 1;
            }
            Instruction::Increment => {
                tape[*data_pointer] += 1;
            }
            Instruction::Decrement => {
                tape[*data_pointer] -= 1;
            }
            Instruction::Write => print!("{}", tape[*data_pointer] as char),
            Instruction::Read => {
                let mut input: [u8; 1] = [0; 1];
                std::io::stdin().read_exact(&mut input).expect("failed to read stdin");
                tape[*data_pointer] = input[0];
            }
            Instruction::Loop(nested_instructions) => {
                // Execute the loop
                while tape[*data_pointer] != 0 {
                    run(&nested_instructions, tape, data_pointer);
                }
            }
        }
    }
}


pub fn std_input() {
    let mut input_buffer = String::new();

    // Get input from user
    println!("Enter input (Single Line): ");
    io::stdin().read_line(&mut input_buffer).expect("failed to read input");
    // Input validation
    if input_buffer.len() == 0 || input_buffer == "\n" {
        println!("No input given or invalid input");
        return;
    }
    println!("Input: {}", input_buffer);

    // Lex input into opcodes
    let opcodes = lexer::lex(input_buffer);
    // Parse opcodes into program
    let program = parser::parse(opcodes);
    // Set up environment and run program
    let mut tape: Vec<u8> = vec![0; 1024];
    let mut data_pointer = 512;
    run(&program, &mut tape, &mut data_pointer);
}
