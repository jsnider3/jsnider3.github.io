---
layout: post
title:  "Running into the Spike: A Retrospective"
date:   2015-06-22 12:00:00
comments: True
categories: update opinion web-development
---

#### Intro

I recently made a project to list the languages a GitHub user has in
all of their repositories. You can find it at
[https://www.joshuasnider.com/GitHubBOC](https://joshuasnider3.com/GitHubBOC).
This is just the thoughts I wrote down while making it organized in
a moderately presentable way. 

#### Motivations

I’ve never been more intimidated in my life than when I try to learn
something and don’t know where to start. I’ve felt this feeling when
learning a programming language completely different than one I already
know, when trying to study quantitative finance, and whenever I try to
learn web or mobile development.

I had a couple motivations for learning web development which can be
separated cleanly into an actual desire to make
[this code](https://joshuasnider.com/GitHubBOC) and inspiration
I’ve received from the wider community. First among my intrinsic
motivations, is an actual desire to have a tool to show the language breakdown
among all of my GitHub repos, so I can use it myself. I tried asking
[Stack Exchange](http://webapps.stackexchange.com/q/75027/),
if they knew someone who already did it a couple months ago, but none of
the similar work out there met my needs so I did it myself. Second, I
feel I’ve reached the point in my career as a computer scientist where my
skills need to be broad enough that I am able to do web development when
called upon and this project was of a good scope for learning AngularJS.
My third intrinsic motivation came from my interest in comparative
programming languages, the event-based models common to web programming are
substantially different from the functional, imperative, and object-oriented
paradigms I’ve experienced in other languages.

Extrinsic motivation for this project came from a few sources. I’ve
recently started showing off my work on Hacker News and think if I had
some more visually appealing work it would be well received. I was also
inspired by [this passage](http://genius.com/4126913/Genius-the-genius-isms/Run-into-the-spike)
from a blog about always doing whatever you least like to do which also
inspired the title. Lastly, I was inspired by [this blog post](http://carl.flax.ie/dothingstellpeople.html).
The idea of “doing cool things and telling people” isn’t specific to
web development or even computer science, but it was a good kick to get
me to actually do it.

All in all, I had a project idea and sufficient motivation to finally sit
down and learn some web development. Getting started was a bit of a
challenge and I lost some internet points by asking noobish questions
on Stack Overflow, but I feel pretty good now and expect to finish this
project before New York. I swear that I will not rest until I get a star
on my JavaScript GitHub repos, because after all worthless internet points
are the most valuable thing in the universe.

#### Obstacles

Like all software projects, this one faced setbacks and delays. I
originally started working on a node.js app and got everything but the
pretty pictures done before finding out that you can’t run server-side
code on GitHub pages. At this point, I decided to switch to a d3js and
angular app. I knew absolutely nothing about these, but I worked through
the “Intro to JavaScript” and “AngularJS” tutorials on Codecademy. I’m
definitely not the target audience for the “Intro to JavaScript” tutorial,
but it did expand my knowledge of JavaScript’s OOP support. The "AngularJS"
tutorial was much more interesting. The idea of binding actions directly to
pieces of html seems extremely powerful and I’d really like to know both
what kind of black magic is done to actually implement it and what the
practical limitations of it are. I eventually ended up using uvCharts
(which is built on d3) for my charts because I saw an example “StackedBar”
chart that was exactly what I wanted to do. There was one problem with it
that took some time for me to discover, the dataset needs to have a value
specified for each category(not actually the category) and they need to be
in the same order for each category. There’s still one bug in the project
that is a huge pain, where because we’re not logged into GitHub it will
throttle our GitHub requests after the third or fourth person. The solution
to that one is to just have the user log into GitHub when they want to use
it, this would overcome the throttling issues and we’d be able to show them
their own repos (instead of mine) by default which would be better. I had
some difficulty catching the errors that we receive when we’re being
throttled, but I choose to blame that on inadequate documentation.

#### Conclusions

From my previous experience as a teaching assistant, I don’t have a very
good opinion of people who want to look at working code while writing their
own similar code. For most of my life, I’ve thought these people are at
worst plagiarists and at best cargo cultists. Neither option being
associated with competence, but at least in this project I saw the value
of having a few working examples from Codecademy which I could reference
when I didn’t know why something wasn’t working, but couldn’t make that
confusion isn’t a question worthy of Stack Overflow. I also spent a couple
hours on Skillport which is a tutorial service provided by my employer,
but it was nowhere near as helpful as Codecademy and Google. I think the
value of looking at working code depends on the subject matter, in areas
like computer vision and AI coming up with the idea behind the code takes
95% of the thought and reading someone else’s code is less useful than
picking up a textbook. In something extremely visual like web programming
the actual implementation of a beautiful website is of much more importance
than the ability to sketch one out on paper.

This project also made me install and setup a LAMP server which I use to
debug JavaScript in the browser and was a learning experience to set it up
correctly.

One thing that was also interesting about JavaScript was that there’s a
lot of asynchronous functions that take callbacks. The reason for this is
that waiting for a response from a server takes forever compared to running
any reasonable amount of code and waiting for someone who may be on the
other side of the globe to respond to you when you could be doing something
productive is a guaranteed way to kill performance. A language that only
did asynchronous callbacks would be pretty mind-warping, what are the odds
Erlang is like that?

I’d be surprised if there’s anyone actually reading this, but I have a
message for them: If you learn anything from this blog post, you should
learn to find whatever challenge you find most intimidating, even,
especially in fact, if it’s not programming and just tackle it now,
immediately, and head on. Especially, if it's commenting on this post.
