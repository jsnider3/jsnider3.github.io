---
layout: post
title:  "Esovectors"
date:   2015-08-08 12:00:00
comments: True
categories: update data-structures
---

In practical terms, resizable arrays (implemented by `std::vector` in
C++)<sup>1</sup> are a very good data structure and in most respects compare
favorably to linked lists. They fit better into memory caches, have less
overhead, and support indexing in constant time. Their actual downsides are that
inserting and deleting in arbitrary locations takes linear time. This is
because we need to move up to the entire array when we change the first
element in it. In addition, we will also need to move the entire array
when it changes size too much. The reallocation amortizes away to be a
constant time, but it’s still an occasional<sup>2</sup> `O(n)` for
insertions/deletions within a constant of the end.

I’ll introduce a variant of the resizable array which allows us to have
constant `O(n)` complexity for insertions and deletions at the end and see
if it can solve the issue of arbitrary changes taking `O(n)` time. I call
these “esovectors” as they are an esoteric version of a vector.<sup>3</sup>

The way current resizable arrays work is that when you reach a certain
point, you allocate an entirely new block of memory, copy everything over
to it, and then free the block of memory you were previously used. This
works well, but still means that you’re obliged to copy blocks of unbounded
size. An alternative approach is to when we reach
a limit, allocate a second array, copy a constant amount over, and then copy
another constant of us over. By adjusting the point at which we reallocate
and the amount that we copy over, we can make sure that our old array is
empty at the same time our new array becomes full. For indexing operations,
we just need to check which buffer the nth element would be in and then index
into that one as normal. Like in normal vectors, indexing continues to take
`O(1)` time.

The additional space needed by this is `O(n)`, which matches the `O(n)` used
by normal vectors, but it’s a worse `O(n)` since we need to maintain a new
array almost twice as big as our old away, whereas vectors are at worst
half full.<sup>4</sup>

However, a critical issue to consider is the cost of memory allocation,
which greatly exceeds the cost of writing a single element of an array,
though is also trivially fast. The running time of `malloc` is entirely
dependent on the implementation chosen by the system, but in most cases
is unrelated to the number of bytes we are requesting. We shall assume
that our `malloc` uses two level segregate fit<sup>5</sup> which is `O(1)`
time. Therefore, `malloc` does not affect our worst case appending performance.

I've shown how to modify dynamic arrays to support appending and removing
from the end in constant time, not just amortized constant time. Another
data type that is frequently implemented using dynamic arrays is the
double ended queue, which in addition to supporting the same operations
as dynamic arrays in the same time, they support popping and inserting
at the beginning in amortized constant time. I will leave it as an exercise
to the reader how to extend esovectors to support this behavior in
non-amortized constant time.<sup>6</sup>

--------

**Footnotes:**

1. They have many names: array lists, growable arrays, etc. Wikipedia calls
  them [dynamic arrays.](https://en.wikipedia.org/wiki/Dynamic_array)

2. How often this occasional reallocation happens depends on the growth factor
  `g` which determines how much bigger the array becomes each time it's
  reallocated. There is some interesting reading on this topic
  [here.](https://github.com/facebook/folly/blob/master/folly/docs/FBVector.md)

3. I have an implementation and test cases 
  [here.](https://github.com/jsnider3/Workspace/tree/master/Esovector)

4. The worst case for both is when we have `n` elements in an array of size `n`
  and try to insert an additional element. Traditional vectors allocate
  a new array of size `2n` and then use it to store `n + 1` elements.
  For esovectors we allocate a new array of size `2n`, put 2 elements
  in it, and leave `n - 1` elements in our old array.<sup>7</sup>

5. Introduced in [this paper.](http://www.gii.upv.es/tlsf/files/ecrts04_tlsf.pdf)

6. Read this as "I want someone else to do my work for me."

7. This assumes a growth factor of 2, which is common but inefficient.
  See the link in footnote 2.
