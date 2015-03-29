---
layout: post
title:  "What does the title mean anyway?"
date:   2015-03-29 01:17:54
categories: update haskell
---

There's a short answer and a long answer to that question.
The short answer is that `(\x -> "Blog")` defines an anonymous function
in Haskell that takes a simple argument of arbitrary type, ignores it, 
and returns "Blog".

The long way to define this function would be as:
{% highlight haskell %}
foo :: a -> String
foo a = "Blog"
{% endhighlight %}

For those unfamiliar with Haskell's lazy evaluation, this function has
a strange feature. Calling `foo` with  an `a` designed to crash, such as
`foo undefined` or `foo (error "DIE!")` will run perfectly fine.
