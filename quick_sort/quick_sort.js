function quickSort(arr) {
    if (arr.length <=1 ) return arr;

    let left = [];
    let right = [];
    let pivot = arr[arr.length - 1];

    for(let i = 0; i < arr.length - 1; i++) {
        if(arr[i] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }
    return [...quickSort(left), pivot, ...quickSort(right)];
}

// Example usage:
const array = [34, 7, 23, 32, 5, 62];
console.log(quickSort(array)); // Output: [5, 7, 23, 32, 34, 62]


