// const myNums = [64, 34, 25, 12, 22, 11, 90, 5];

// let n = myNums.length;

// for (let i = 0; i < n-1; i++) {
//     for (let j = 0; j < n-i-1; j++) {
//         if (myNums[j] > myNums[j+1]) {
//             myNums[j], myNums[j+1] = myNums[j+1], myNums[j];
//         }
//     }
// }

// console.log(`the sorted array is: ${myNums}`);

function bubbleSort(arr) {
    let len = arr.length;
    for (let i = 0; i < len-1; i++) {
        let swapped = false;
        for(let j = 0; j < len-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                swapped = true
            }
        }
        if(!swapped) {
            break;
        }
    }
    return arr;
}
console.log(bubbleSort([7, 3, 9, 12, 11]))

