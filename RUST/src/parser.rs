/**
 @Author: Murtadha Marzouq
 @description: This file is responsible for parsing the opcodes into instructions
 # Lexical structure: the structure of the tokens, or words, of a language -Related to, but different than, the syntactic structure
 # Scanning phase: the phase in which a translator collects sequences of characters from the input program and forms them into tokens
 # Parsing phase: the phase in which the translator  processes the tokens, determining the program's syntactic structure
 */


use crate::OpCode;
use crate::Instruction;
/**
# Steps:
# 1. Read the opcodes. # - Read the opcodes from the input file. # - If a loop is found, parse the opcodes inside the loop and add the resulting instruction to the vector. # - If a loop is not closed, panic. #
# 2. Create a vector of instructions. # - Populate the vector with the instructions that will be executed. # - If a loop is found, parse the opcodes inside the loop and add the resulting instruction to the vector. # - If a loop is not closed, panic. #
# 3. Return the vector of instructions. # - The vector of instructions is the program that will be executed.
 */
pub fn parse(opcodes: Vec<OpCode>) -> Vec<Instruction> {
    let mut program: Vec<Instruction> = Vec::new();
    let mut loop_stack = 0;
    let mut loop_start = 0;

    for (i, op) in opcodes.iter().enumerate() {
        if loop_stack == 0 {
            let instr: Option<Instruction> = match op {
                OpCode::IncrementPointer => Some(Instruction::IncrementPointer),
                OpCode::DecrementPointer => Some(Instruction::DecrementPointer),
                OpCode::Increment => Some(Instruction::Increment),
                OpCode::Decrement => Some(Instruction::Decrement),
                OpCode::Write => Some(Instruction::Write),
                OpCode::Read => Some(Instruction::Read),

                OpCode::LoopBegin => {
                    loop_start = i;
                    loop_stack += 1;
                    None
                }

                OpCode::LoopEnd => panic!("Unexpected loop end"),
            };

            match instr {
                Some(instr) => program.push(instr),
                None => (),
            }
        } else {
            match op {
                OpCode::LoopBegin => {
                    loop_stack += 1;
                }
                OpCode::LoopEnd => {
                    loop_stack -= 1;

                    if loop_stack == 0 {
                        program.push(Instruction::Loop(parse(opcodes[loop_start + 1..i].to_vec())));
                    }
                }
                _ => (),
            }
        }
    }

    if loop_stack != 0 {
        panic!(" {} loop(s) not closed", loop_stack);
    }

    program
}
