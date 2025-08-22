function binarySearchRecursive(arr, target, left = 0, right = arr.length - 1) {
    if (left === 0 && right === arr.length -1) {
        arr = arr.slice().sort((a, b) => a - b)
    }

    console.log(arr)
    if (left > right) return -1

    let mid = Math.floor((left + right) / 2)

    if (arr[mid] === target) {
        return mid
    }

    if (arr[mid] < target) {
        return binarySearchRecursive(arr, target, mid+1, right)
    } else {
        return binarySearchRecursive(arr, target, mid-1, left)
    }
}

console.log(binarySearchRecursive([4, 3, 6, 8, 2, 1], 6))