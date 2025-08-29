let arr = [1, 2, 3];
arr.push(4)
console.log(arr);

arr.pop()
console.log(arr);

arr.unshift(0)
console.log(arr);

arr.shift()
console.log(arr);

arr.splice(1, 1, 'x')
console.log(arr);

let sub = arr.slice(0, 2);
console.log(sub);