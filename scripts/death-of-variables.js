
let ambiguousVariable = 0.0

let doSynchronousWork = (anIdentifierThatMatters)=>{
    ambiguousVariable.id = anIdentifierThatMatters;
    performGenericActionThatDependsOnATransactionalValue();
}

let performGenericActionThatDependsOnATransactionalValue =  () =>{
    return new Promise((resolve, reject)=>{
        ambiguousVariable += 1;
       sleep(75).then(()=>{
        console.log("i slept");
       
        if(ambiguousVariable === 1.0){
            resolve("all is well in serial land");
        }else{
            reject('I mean, it looks legit to me');
        }});
    })
}

for(var iterations = 0; iterations < 100; iterations++){
    doSynchronousWork();
    console.log("synchronousWork " + iterations + " completed");
}

console.log("All synchronousWork completed");

