var object1 = { value: 10 };
var object2 = object1;
var object3 = { value: 10 }

console.log(object1 === object2);
console.log(object1 === object3);

object1.value = 15;
console.log(object1.value);
console.log(object2.value);
console.log(object3.value);

//objects are called reference types - they are non primitive types
//primitive types are: numbers, booleans, strings, undefined, null etc

//primitive - means was created by the Languages, eg comes with the language - JS
//non-primitives (reference types) - created by programmers.
