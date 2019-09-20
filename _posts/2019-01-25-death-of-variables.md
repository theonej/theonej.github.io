---
layout: default
title: Death of Variables?
---

# On the death of variables

Variables, specifically member variables, make my code less understandable and more complex.

I was doing a code review today, and came across a piece of code that I do not think is uncommon.

I see this most frequently with to mid-level developers that are starting to use asynchronous patterns for the first time.

Here's some example code:
    
    
        let ambiguousVariable = 0.0

        let doSynchronousWork = (anIdentifierThatMatters)=>{
            ambiguousVariable.id = anIdentifierThatMatters;
            performGenericActionThatDependsOnATransactionalValue();
        }

        let performGenericActionThatDependsOnATransactionalValue =  () =>{
            return new Promise((resolve, reject)=>{
                ambiguousVariable += 1;

                callAnExternalResourceThatAverages75ms();

                if(ambiguousVariable === 1.0){
                    resolve("all is well in serial land");
                }else{
                    reject('I mean, it looks legit to me');
                }
            })
        }
    

There is a subtle problem here that becomes apparent with the following code:

    
        for(var iterations = 0; iterations < 100; iterations++){
            doSynchronousWork();
            Console.log("synchronousWork " + iterations + " completed");
        }

        Console.log("All synchronousWork completed");
    

    