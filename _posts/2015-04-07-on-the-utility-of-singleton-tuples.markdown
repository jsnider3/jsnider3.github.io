---
layout: post
title:  "On the Utility of Singleton Tuples"
date:   2015-04-07 12:00:00
categories: update theory
---
Formally, a tuple is an ordered list of elements. As a type, its elements 
may have arbitrary type, but its length is fixed. Many programming 
languages (and almost all functional programming languages) have 
them, while others prefer the programmer create structs or objects instead.
 
Most tuples used in code have between two and four elements. It’s a 
huge pain to read and maintain code with extra-large tuples and 
anything that needs to be that large starts to accumulate helper 
methods which would be useful to wrap up in a class/module/namespace.
 
The tuple containing zero elements is formally known as the unit type. 
In code, it sees uses as a dummy argument to functions (OCaml), as a 
placeholder for the empty list (Lisp), and as a representation of 
`Void` (Swift).
 
The tuple containing a single element is known as a singleton. Despite 
having a strong mathematical foundation, very few languages make the 
distinction between a singleton of a type and the type itself. In all 
the languages I know of where tuples are created by putting parentheses 
around a comma-seperated list trying to create a singleton tuple will 
result in the parentheses being ignored. C# makes the distinction through 
it’s `Tuple<T1>` class and Python allows you to make a single tuple 
through adding a comma (i.e. `(5,)`).
 
The most likely reason for the reluctance of language designers to include 
the singleton tuple, is the lack of scenarios where it would come in 
handy. It’s certainly convenient if you’re a type theorist, but other than 
that the only case where it might be useful is in Python where tuples are 
constant; if you absolutely positively needed a variable in Python to be a 
constant you could wrap it as a tuple.
 
If you know scenarios where a singleton tuple would be useful, you should 
leave a comment below.  
