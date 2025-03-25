//using the 'for' loop

const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit_len = fruits.length;

for (let i = 0; i < fruit_len; i++) {
    console.log(fruits[i])
}

//lets try using the Array.forEach() function

const fruits2 = ["Banana", "Orange", "Apple", "Mango"];
// fruits.forEach(myFunc);
// function myFunc(value) {
//     console.log(value)
// }
fruits2.forEach((fruit, index) => {
    console.log(`${index + 1}: ${fruit}`);
});

const numbers = [1, 2, 3];
numbers.forEach(num => console.log(num * 2))


let users = [
    { name: 'Alice', active: false },
    { name: 'Bob', active: false }
];
users.forEach(user => user.active = true);
console.log(users)