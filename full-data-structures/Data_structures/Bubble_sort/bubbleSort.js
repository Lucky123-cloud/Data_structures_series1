function bubbleSort(arr) {
    const a = arr.slice(); //don't mutate input
    const n = a.length;

    for ( let i = 0; i < n - 1; i++) {
        let swapped = false;
        for (let j = 0; j < n - 1; j++) {
            if (a[j] > a[j + 1]) {
                //swap
                [a[j], a[j+1]] = [a[j + 1], a[j]];
                swapped = true;
            }
        }

        if (!swapped) break;
    }
    return a;
}

console.log(bubbleSort([5, 1, 4, 2, 8]));

//worst case: O(n^2);
//Best case: O(n)
