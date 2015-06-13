---
layout: post
title:  "Compiling Uncool to the JVM with Scala"
date:   2015-06-11 12:00:00
comments: True
categories: update scala uncool compiler
---

I recently made a compiler in Scala that takes UnCool code and targets
the JVM. Its source is [here](https://github.com/jsnider3/Scales). I made
this compiler to gain a deeper understanding of Java development and
learning how to handwrite JVM code helped me understand James Gosling’s
mind. Additionally, I wanted to learn one of the functional JVM languages.
A friend suggested Clojure, but I felt it was too Lispy for me. What
finally sold me on Scala was seeing a few job ads from companies I want to
work for that were looking for Scala engineers.

Writing a compiler might seem like a massive undertaking to many people,
but it’s a lot easier than many think and I have enough experience
implementing programming languages that writing a compiler is enough to
“battle test” my knowledge of a language I’m trying to learn without
taking an excessive amount of time. I already had an IA32-targeting
compiler for UnCool written in Java
[here](https://github.com/jsnider3/Uncool), though it wasn’t much help
for this project. That was partly because a lot of a compiler is
architecture dependent and partly because the parsing differs
substantially between Java’s yacc/JFlex and Scala’s parser combinators.
The main reason to not reuse work from my old compiler is that I have grown
as a programmer substantially since I wrote the original program and it
would have held me back to copy ideas from it.

While building the compiler, I used a development methodology similar to
test-driven development, with a Travis build running as quickly as
possible. I copied the test cases from my old IA32 compiler project and
iterating from simplest to most complex wrote the code needed to make them
pass. There was a five-step cycle for adding a feature:  
1. Parse the test source code correctly.  
2. Generate valid jasmin code.  
3. Improve the code generation until the java verifier would accept it.  
4. Continue editing until the output from running the code was correct.  
5. Nod approvingly and move on to the next test case.  
This development cycle allowed me to keep the build running while still
verifying that I was making forward progress without regression.

Obviously, the project had challenges which I worked to overcome. Starting
out, I had some trouble with Scala's parser combinators which I solved by
seeking help from the StackOverflow community. Later, when I was close to
finishing if-statements I ran into an issue with my code putting the java
stack in an inconsistent state. That is, depending on which branch of the
if-statement, the quantity and types of variables would differ on the
stack. This possibility of an inconsistent state is prohibited by the java
class verifier because it is not type safe. My solution was to track of
how much each expression  pushes onto the stack and then pop everything
off that was not going to be used. At one point, when trying to allocate
local variables, I had a brief panic attack when I thought the number of
local variables in the JVM was limited to five of each type. This was
because I saw the instructions `iload_3`, `aload_0`, and `iload_2` and
tried to extend them out arbitrarily, to say `iload_12`. This was a
misunderstanding on my part: The `iload_#` instructions are not a single
instruction that take a number as an argument but are actually separate
instructions optimized for the first few locals. The correct instructions
for working with arbitrary local variables are `iload #`, `istore #`,
`aload #` and `astore #`. I continued my habit of using makefiles for all
programming languages, instead of taking the time to actually learn how to
use `ocamlbuild` or `sbt`. This made me waste an excessive amount of time
waiting for code to compile, so I should just bite the bullet for my next
project.

There are some bugs I know of that aren't covered by the test cases: it
will fail on methods with more than 32 local variables and if-else
expressions where the two branches typecheck to classes related through
inheritance. Additionally the parser doesn’t take into account operator
precedence. Even with these bugs, I chose to stop coding now when it
passes all of the test cases from the previous project, because I wanted
the experience to be as comparable as possible to writing my old one.

From my short time of working with Scala, I gained a strong appreciation
of it. It has the terseness expected of good functional languages, has
literally every feature I want (notably case classes and enums, which are
the main thing I find lacking in Python) and has a nice built-in library
both from the libraries provided by its creators and from being compatible
with the JVM. I can see why it's well-liked among its community.

The JVM itself is also a neat piece of work. The idea of an "assembly"
language with built in type-safety is a pretty powerful one. Besides the
large amount of money Sun spent promoting it, the brilliance of the JVM is
a key component in the popularity of languages that target it.

In the future, I plan on getting involved with CPython's development to
make something useful out of my passion for programming languages and give
back to the community. Thanks for reading.

