---
layout: default
title: What is the business case for adopting functional programming?
---

# Why functional programming (FP for the context of this post)?

This is not going to be another post about what FP is, and why it has comparitive advantages over some other styles.

If that is what you are looking for, please take a look at these references:

[Practical functional code in python](https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming])
This post displays insight into not only how FP is used, but also why it is popular.  The section on `Don’t iterate over 
lists. Use map and reduce.` has some great examples of how to apply functions to lists.  The progression of built in functions to custom 
<in-line>functions</in-line> as lambdas provides an intuitive example of the balance of conciseness and function that contributes to python's 
popularity.

[Lambdas in c++]([)https://medium.com/@DakshHub/lambdas-the-companion-of-modern-c-b7dfd43b5abb)
![lambdas in c++](../../../img/c++lambdas.png) For fun, google `lambdas in c++` followed by `FP inc++`.  The results are geared towards very different audiences.

This article has a good section on the basics of FP, an explanation (and samples) of how c++ approaches FP.  
The discussion on `Why use Functional Programming?` describes the mechanical and efficiency advantages of FP.  
What I am hoping to do here is to discuss the financial, temporal and human advantages that, IMO, make a more convincing
argument for the adoption of some FP practices.

##Financial Impact
It costs money to adopt functional practices in most cases.  There is usually the direct cost of bringin in a new team member that is familair
and experienced with functional practices in a *production environment*.  Candidates without production experience should be considered, but not 
as change agents or leads on the project.

Secondary financial costs can be identified in the delay to schedule while new team members are being onboarded, compounded by the learning curve
of the team as new concepts are being introduced and implemented.  Successive costs can accrue from mistakes on the part of both the new team members, not understanding the existing system adequately, and the existing team making errors in implemetation of the new patterns and parctices (note that the new team members who are introducing these new technologies are themselves also subject to costs associated with mistaken implementation).

The question then becomes: `If I already have a functioning production environment, that is generating revenue, why would I incur these costs?`
read: `How does that make me more money?`

And here is where I think the best case can be made for the business case to adopt FP practices.  The elements to the cost equations for 
most businesses I have worked for look something like this:

    T = Time to revenue from concept
    D = dev team salaries/costs
    QA = A fraction ranging between 0 and &#8734; that represents the ration of QA engineers to developers
    I = Incremental profit from new initiative
    R = revenue
    B = Time boundary for the go-live event
    H = Range of hours to examine on both sides of the go-live time boundary

First we calculate the total Costs (C) for the initiative

    C = T(D + (TD * QA))
    
Next we calculate the amount of profit that the initative recognizes by comparing tow timespans, which must be separated by a time boundry that represents the go-live time of the initiative.

    I = R(B + H) - R(B - H)

If this number is positive, you have made money.  If it is negative, you have lost money.  

Looking at the equations, there are a few levers you can pull to minimize C and maximize I.  Looking at T, we can immediately move C by reducing T.
Since QA is a multiplier on the additional dev costs (TD * QA), minimizing QA can provide returns to the bottom line.  The benefits of test automation are beyond the scope of this topic.  The argument for FP practices in this area are:
- Functional code behaves in a more deterministic manner than code that allows side effects
- Functional code naturally lends itself to testability by it's inherent structure and boundaries


