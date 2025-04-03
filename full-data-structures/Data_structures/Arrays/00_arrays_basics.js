const strings = ['a', 'b', 'c', 'd'];
//4 *4 = 16bytes of storage 

strings[2] // 'c'

//methods in arrays:
//push - add something at the end of array
strings.push('e'); // O(1);

//pop() - opposite of push removes last items in the array
strings.pop(); //O(1);

//unshift - adds something at the begining of the array
strings.unshift('x'); // O(n);

//splice - adding something at the middle of the array
strings.splice(2, 0, 'alien'); //O(n);
// splice takes 3 params:
    // - starting place - where to start(or where the replacemnt would occur)
    // - deleteCount, - essetiually how many items do you want to delete from the chosen starting place
    // - what we want to add in the starting place. for our case we want to add 'alien'.

//shift() - adding something at the begining of an array
strings.shift();
console.log(strings);