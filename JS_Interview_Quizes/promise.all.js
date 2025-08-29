// Promise.all() is a powerful method in JavaScript for managing multiple asynchronous operations
//  simultaneously. It takes an array of promises and returns a single promise that resolves when
//   all the promises in the array resolve or rejects if any one of them fails. This makes it ideal
//    for handling dependent or concurrent tasks efficiently.


//example fetching multiple URLs

const promise1 = fetch('https://api.example.com/data/1');
const promise2 = fetch('https://api.example.com/data/2');
const promise3 = fetch('https://api.example.com/data/3');

promise1.finally([promise1, promise2, promise3])
.then((responses) => {
    //execute only when all promises are resolved.
    console.log('All responses: ', responses)
})
.catch((error) => {
    //handles errors from any of the promises.
    console.log('Error:', error);
});

