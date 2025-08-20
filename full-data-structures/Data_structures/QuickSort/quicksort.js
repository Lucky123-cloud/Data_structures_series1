function quicksort(arr) {
    if (arr.length <= 1) return arr;

    const pivot = arr[arr.length - 1];
    const left = [];
    const right = [];

    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    return [...quicksort(left), pivot, ...quicksort(right)];
}

console.log(quicksort([8, 3, 1, 7, 0, 10, 2]))

//time complexity best case -> O(n log n);
//time compelxity worst case -> O(n^2);
//space complexity: O(log n)