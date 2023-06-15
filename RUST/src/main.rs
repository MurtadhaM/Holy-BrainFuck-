/**
 * # Author: Murtadha Marzouq
 * # Description: hbf or (Holy Brain Fuck ) is a small project I created to help me learn more about programming languages
 * # Function: It takes in a brainfuck source code and interprets it in Rust like a. This maybe a front to all thing good and holy but it was fun. It is like cursing but in shaksprian style
 * # Resources: 
 * # 1. https://doc.rust-lang.org/book/
 * # 2. https://en.wikipedia.org/wiki/Brainfuck
 * # 3. https://benwendt.ca/articles/converting-to-bf/
 * # 4 . https://github.com/usaikiran/brainfuck-visualizer
 * # 5. http://www.muppetlabs.com/~breadbox/bf/
 * # 6. https://esolangs.org/wiki/Category:Brainfuck_derivatives
 * # 7. http://www.chriswarbo.net/blog/2014-12-22-minimal_languages.html
 * 
 *
*/
 
use std::{ env, fs };
use interpreter::std_input;
use crate::interpreter::run;
mod lexer;
mod parser;
mod interpreter;
#[derive(Debug)]
#[derive(Clone)]
pub enum OpCode {
    IncrementPointer,
    DecrementPointer,
    Increment,
    Decrement,
    Write,
    Read,
    LoopBegin,
    LoopEnd,
}
#[derive(Debug)]
#[derive(Clone)]
pub enum Instruction {
    IncrementPointer,
    DecrementPointer,
    Increment,
    Decrement,
    Write,
    Read,
    Loop(Vec<Instruction>),
}

fn init(){
    let args: Vec<String> = env::args().collect();
    if args.is_empty(){
        println!("usage: hbf -f <filename>  -e <code> -d <debug> -o <output> -i <input> -h <help>");
        return;
    }
    let mut _debug = false;
    let mut output: String = String::new();
    let mut help: bool = false;
    let mut code = false;
    let mut input: bool = false;
    let mut filename = String::new();

    for arg in args.iter() {
        if arg == "-f" {
            filename = args
                .clone()
                .join(" ")
                .split("-f")
                .collect::<Vec<&str>>()[1]
                .split(" ")
                .collect::<Vec<&str>>()[1]
                .trim()
                .to_string();
        }
        if arg == "-c" {
            code = true;
        }
        if arg == "-d" {
            println!("I do not do anything, but make you feel smarter");
            interpreter::show_debug(filename.clone());
            return;
        }
        if arg == "-o" {
            output = args
                .clone()
                .join(" ")
                .split("-o")
                .collect::<Vec<&str>>()[1]
                .split(" ")
                .collect::<Vec<&str>>()[1]
                .trim()
                .to_string();
        }
        if arg == "-i" {
            input = true;
        }
        if arg == "-h" {
            help = true;
        }
    }

    if args.len() == 0 && !help {
        println!("usage: hbf -f <filename>  -e <code> -d <debug> -o <output> -i <input> -h <help>");
        return;
    }
    if code && filename.len() > 0 {
        println!("cannot use -e and -f at the same time");
        println!("usage: hbf -f <filename>  -e <code> -d <debug> -o <output> -i <input> -h <help>");
        return;
    }

    if help {
        println!("usage: hbf -f <filename>  -e <code> -d <debug> -o <output> -i <input> -h <help>");
        println!("-f <filename> : file to execute");
        println!("-e <code> : code to execute");
        println!("-d <debug> : debug mode");
        println!("-o <output> : output file");
        println!("-i <input> : input file");
        println!("-h <help> : help");
        return;
    }

    if input {
        std_input();
        return;
    } else if filename.len() > 0 {
        println!("Reading: {}", filename);
        if output.len() > 0 {
            println!("Output File: {}", output);
        }
        let file_contents = fs::read_to_string(filename.clone()).expect("failed to read file");
        let opcodes = lexer::lex(file_contents);
        let program = parser::parse(opcodes);
        let mut tape: Vec<u8> = vec![0; 1024];
        let mut data_pointer = 512;
        run(&program, &mut tape, &mut data_pointer);
        return;
    }
}

fn main() {
    
    init();
}
