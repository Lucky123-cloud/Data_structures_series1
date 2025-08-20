function linear_search(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i;
        }
    }
    return -1;
} 

console.log(linear_search([4, 2, 1, 7, 5, 9], 7))