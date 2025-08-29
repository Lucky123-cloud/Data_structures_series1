const myNum = [1, 4, 6, 7, 0, 3, 4];

// let minVal = myNum[0];

// for (let i = minVal; i < myNum.length - 1; i++) {
//     if (i < minVal) {
//         minVal = i;
//     }
// }

function minimumVal(arr) {
    let minVal = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < minVal) {
            minVal = arr[i];
        }
    }

    return minVal
}
console.log(minimumVal([2, 4, 5, 1, 7]))