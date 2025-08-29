console.log(0);
console.log(1);
count = 2;

function fibonacci(prev1, prev2) {
    if (count <= 19) {
        newFib = prev1 + prev2;
        console.log(newFib);

        count++;
        fibonacci(newFib, prev1)
    } else {
        return;
    }

    
} 

fibonacci(0, 1);