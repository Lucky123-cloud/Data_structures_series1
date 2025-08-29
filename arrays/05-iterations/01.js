let nums = [6, 9,  1, 2, 3, 4, 5];

nums.forEach((x, i) => {
  console.log(`index ${i}: ${x}`);
});

nums.forEach(n => console.log(n*2));

let doubled = nums.map(n => n * 2);
console.log(doubled);

let even = nums.filter(n => n % 2 === 0);
console.log(even);

let sum = nums.reduce((a, b) => a + b, 0);
console.log(sum);

let allEven = nums.every(n => n % 2 === 0);
console.log(allEven);

let someEven = nums.some(n => n % 2 === 0);
console.log(someEven);

let array = nums.sort();
console.log(array);
