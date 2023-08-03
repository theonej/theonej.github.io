---
layout: default
title: Why is naming things hard?
---

# Naming things is hard?

You have probably read [somehwere](https://martinfowler.com/bliki/TwoHardThings.html) that naming things is hard.

I was slacking with one of the guys I work with, who I really respect, about naming things.  He was reading some node code his team wrote ~ 6 months ago, and he was auditing it for a new initiative.

At one point he slacked me something like `holy shit.  there's litterally a variable here named 'variable'`.  We had a good laugh about naming things, but it got me thinking.

Why is naming things hard?  I mean, we're just assigning a name to something so we can reference it later.

Here's what I think:  Naming things is hard, because naming things is design.

In programming, we use metaphors as a bridge between the human mind and the CPU.  If you are working on a system with heavy data access, you might use a [repository metaphor](https://dev.to/kylegalbraith/getting-familiar-with-the-awesome-repository-pattern--1ao3#targetText=Implementing%20Repository%20Pattern,the%20top%20of%20data%20access.&targetText=With%20the%20repository%20pattern%20we,logic%20can%20leverage%20those%20abstractions.).  This is a great pattern because it's easy to have a concept of a repository as something you put things in and get things out of.  The computer doesn't need to see things that way.  It just needs the instructions on how to create the channel, what protocol to use, what data to pass, which operation to execute, etc...

Every time we create a new *thing* in our code, we are adding a metaphor and its' associated meaning into the programmers brain, which they have to load up every time they want to work on the code.  If the collection of accumulated metaphors becomes too convoluted, or if the metaphors don't relate to each other properly to form a coherent picture, it becomes difficult for the programmer to load the system into their mind, which reduces their ability to easily navigate the program.

One thing that I've found on my teams is that peer review can help with this problem.. If the metaphors don't make sense, it should be pretty clear to someone else that is reviewing the code.  I generally set up reviews to require at least 2 reviewers before a PR.

