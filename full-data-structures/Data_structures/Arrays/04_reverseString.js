//N/B: treat all strings as arrays


function reverse1(str) {
    return str.split("").reverse().join("");
}

function reverse2(str) {
    return [...str].reverse().join("")
}

function reverse3(str) {
    // Check input
    if (!str || str.length < 2 || typeof str !== 'string') {
        return "Invalid input";
    }

    const backwards = [];
    const totalItems = str.length - 1;

    for (let i = totalItems; i >= 0; i--) {
        backwards.push(str[i]);
    }

    return backwards.join('');
}

// Call and print the result
console.log(reverse2('Hi My name is Lucky')); 
