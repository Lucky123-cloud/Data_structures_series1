function bubblesort(arr) {
    let n = arr.length;
    arr = arr.slice();

    for(let i = 0; i < n-1; i++) {
        let swapped = false;
        for(let j = 0; j < n-1-i; j++) {
            if(arr[j] > arr[j+1]) {
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                swapped = true;
            }
        }
        if(!swapped) break;
    }
    return arr;
}

console.log(bubblesort([64, 34, 25, 12, 22, 11, 90]));


//Worst case time complexity: O(n^2)
//Best case time complexity: O(n) (when the array is already sorted)
//Average case time complexity: O(n^2)
//Space complexity: O(1) (in-place sorting)
