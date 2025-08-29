let prev2 = 0;
let prev1 = 1;

console.log(prev2);
console.log(prev1);

for (let i = 2; i < 18; i++) {
    let newFib = prev2 + prev1;
    console.log(newFib);

    prev2 = prev1;
    prev1 = newFib;
}