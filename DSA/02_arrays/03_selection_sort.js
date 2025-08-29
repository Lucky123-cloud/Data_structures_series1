// my_array = [64, 34, 25, 5, 22, 11, 90, 12]

// let len = my_array.length;
// for (let i = 0; i < len-1; i++) {
//     let min_index = i;
//     for (j = i + 1; j < len; j++) {
//         if (arr[j] < arr[min_index]) {
//             min_index = j;
//         }
//     }

//     if (min_index !== i) {
//         [arr[i], arr[min_index]] = [arr[min_index], arr[i]];
//     }
// }

// return arr

function selectionSort(arr) {
    let len = arr.length;
    for (let i = 0; i < len-1; i++) {
        let minIndex = i;
        for(let j = i + 1; j < len; j++) {
            if(arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        if(minIndex !== i) {
            [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
        }
    }
    return arr;
}

console.log(selectionSort([64, 34, 25, 5, 22, 11, 90, 12]))