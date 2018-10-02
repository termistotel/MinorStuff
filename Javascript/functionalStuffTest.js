// functionsr
const head = ([head, ...tail]) => head
const tail = ([head, ...tail]) => tail
const map = ([head, ...tail], fun = x => x) => head ? [fun(head), ...map(tail, fun)] : []
const filter = ([head, ...tail], testFun = x => true) => head ? (testFun(head) ? [head, ...filter(tail)] : [...filter(tail)]) : []
const reduce = ([head, ...tail], fun, acc) => head ? reduce(tail, fun, fun(acc, head)) : acc
const join = ([head, ...tail], separator = ',') => head ? (tail.length>0) ? [head, separator, ...join(tail,separator)] : [head] : []


// let vs var
let callbacksLet = [];
let callbacksVar = [];
for (let i = 0; i < 2; i++)  callbacksLet[i] = ()=>console.log("let: ", i)
for (var i = 0; i < 2; i++)  callbacksVar[i] = ()=>console.log("var: ", i)


// Tests
console.log(map([3,4,5], x=>2*x))
console.log(filter([3,4,5], x=>x>3))
console.log(reduce([3,4,5], (x,y)=>x+y, 3))
console.log(...join(['kurac', 'palac'], ','))
callbacksLet.forEach(x=>x())
callbacksVar.forEach(x=>x())