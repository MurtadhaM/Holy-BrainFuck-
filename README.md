
# HBF - Holy Brain Fuck!

 <img src="./holy-brainfuck-images/logo-no-background.png" width="100%">

<a href="http://findasnake.com"></a>

---

![](https://img.shields.io/badge/HOLY_BRAIN_FUCK-Introduction-red)

hbf or (Holy Brain Fuck ) is a small project I created to help me learn more about programming languages
Function: It takes in a brainfuck source code and interprets it in Rust like a. This maybe a front to all thing good and holy but it was fun. It is like cursing but in shakespearean style

---
## Resources:

---
![](https://img.shields.io/badge/QuickLinks-Resources-blue)

##### Here are some useful links related to Brainfuck that I used:


- [Article by Ben Wendt](https://benwendt.ca/articles/converting-to-bf)
- [Brainfuck Visualizer Logo](https://github.com/usaikiran/brainfuck-visualizer)
- [The Rust Book](https://doc.rust-lang.org/book/) 
- [The Brainfuck Programming Language](http://www.muppetlabs.com/~breadbox/bf/) ![Brainfuck Programming Language Logo](https://www.google.com/s2/favicons?domain=http://www.muppetlabs.com)
- [Brainfuck Derivatives](https://esolangs.org/wiki/Category:Brainfuck_derivatives) ![Brainfuck Derivatives Logo](https://www.google.com/s2/favicons?domain=https://esolangs.org)
- [Minimal Languages](http://www.chriswarbo.net/blog/2014-12-22-minimal_languages.html) ![Minimal Languages Logo](https://www.google.com/s2/favicons?domain=http://www.chriswarbo.net)

- [Walkthrough Video](https://www.youtube.com/watch?v=4uNM73pfJn0) ![Minimal Languages Logo](https://www.google.com/s2/favicons?domain=http://www.chriswarbo.net)



## Motivations:
![](https://img.shields.io/badge/Motivations-Introduction-yellow)


| Language | Compilation | Memory Management | Performance | Syntax and Semantics | Type System | Paradigms |
| --- | --- | --- | --- | --- | --- | --- |
| <img src="https://www.freecodecamp.org/news/content/images/2021/01/rust-mascot.png"> | Compiled | Ownership and borrowing | Comparable to C++, optimized for performance | C-like syntax with {} and ; | Algebraic data type system with enums, trait bounds, lifetimes, etc. | Functional and imperative |
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1200px-ISO_C%2B%2B_Logo.svg.png" > | Compiled | Manual memory management with new/delete and smart pointers | Comparable to Rust, optimized for performance | C-like syntax with {} and ; | Sophisticated type system with templates, inheritance and operator overloading | Object-oriented, functional and imperative |
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"> | Interpreted | Automatic garbage collection | Slower than Rust and C++ | Clean, simple syntax with indentation for blocks and no ; | Dynamically typed, types assigned at runtime | Primarily object-oriented |

### UML Diagrams:
![](https://img.shields.io/badge/UML-Diagram-blue)


```diff

- C++:
+ FileReader: Reads the file and returns a string
+ Tokenizer: Tokenizes the string and returns a vector of tokens
+ Interpreter: Interprets the tokens and returns the output

```


<img src="./holy-brainfuck-images/UML2.png" width=150%>


<img align="center" src="./holy-brainfuck-images/UML3.png">

## Plan:
![](https://img.shields.io/badge/Plan-STEPS-green)

#### The eight commands are:

| Command | Description |
| --- | --- |
| `>` | Increment the data pointer |
| `<` | Decrement the data pointer |
| `+` | Increment the byte at the data pointer |
| `-` | Decrement the byte at the data pointer |
| `.` | Output the byte at the data pointer |
| `,` | Input a byte and store it in the byte at the data pointer |
| `[` | Jump forward past the matching `]` if the byte at the data pointer is zero |
| `]` | Jump backward to the matching `[` if the byte at the data pointer is nonzero |


## Implementations
![](https://img.shields.io/badge/Languages-Code-purple)

---
### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width=50px> 

```fish
A high-level, interpreted programming language with an emphasis on code readability. It is garbage-collected and dynamically typed.
Implement the interpreter using classes for the different tokens and operations
```
<img src="./holy-brainfuck-images/PYTHON.png">
<img src="./holy-brainfuck-images/UML3.png">


## <img src="https://www.freecodecamp.org/news/content/images/2021/01/rust-mascot.png" width="50px"> 

```fish
a multi-paradigm, general-purpose programming language with a focus on efficiency, type safety, and concurrency. It ensures memory safety by employing a Borrow-Checker.
Implement the interpreter using vectors and immutable variables.
```
<img src="./holy-brainfuck-images/UML2.png">

<img src="./holy-brainfuck-images/RUST.png">

### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1200px-ISO_C%2B%2B_Logo.svg.png" width=50px > 

```fish

A flexible and powerful programming language. Pointers, functions, classes, and templates are all well explained.
Implement the interpreter using vectors and pointers, and iterate over the input stream.

```
<img src="./holy-brainfuck-images/UML1.png">

<img src="./holy-brainfuck-images/C++.png">
---

## POC:
---
![](https://img.shields.io/badge/Summary-Demo-white)


![Demo 1](./holy-brainfuck-images/logo-no-background.png)





## Author
---
<a href="http://findasnake.com">![](https://img.shields.io/badge/Authors-Used-orange)</a>

### Murtadha Marzouq
![Murtadha Marzouq](https://avatars.githubusercontent.com/u/45076915?s=200&v=4)

