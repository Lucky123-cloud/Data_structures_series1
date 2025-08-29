//Log all pairs of array
const boxes = ['a', 'b', 'c', 'd', 'e'];


function logAllPairsOfArray(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            console.log(array[i], array[j])
        }
    }
}

logAllPairsOfArray(boxes)

//what is the big O of this?
//When you see nested loops, we use multiplication:
//what we mean is that when we see O(n) and the innner loop is O(n),
// we multiply and say it is O(n^2)

// O(n^2) - this is called quadratic time.

//this is the Big O(n^2) - This is really horrible, and we need to make it better, and that is where the interviews do come from.
