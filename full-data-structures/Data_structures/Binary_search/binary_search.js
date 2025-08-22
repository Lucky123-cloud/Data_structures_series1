function binarySearch(arr, target) {
    let sorted = arr.sort((a, b) => a - b)
    let left = 0;
    let right = sorted.length - 1;
    console.log(sorted);

    while (left <= right) {
        mid = Math.floor((left + right) / 2);
        
        if (sorted[mid] === target) {
            return mid;
        }

        if (sorted[mid] < target) {
            left = mid + 1 // search right
        } else {
            right = mid - 1 //search left
        }
    }
    return -1;
}

console.log(binarySearch([10, 43, 4, 5, 7, 8], 7))

//this is iterative method
// best case O(1) -> when the elemnt is found at the target
//Wordt case O(log n)

//iterative is the best, because it does not use extra space hence the space complesity is O(1)