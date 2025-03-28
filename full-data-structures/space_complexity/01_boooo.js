function boooo(n) {
    for (let i = 0; i < n.length; i++) {
        console.log('boooooo!')
    }
}

boooo([1, 2, 3, 4, 5])
//what is the time complexity? of course it is Big O(n).
//How about spce complexity? Looking at the function we see that, this function has only
// let i = 0; this is an additional space we are adding. Hence we will say it has a space complexity of O(1)
//lets take another example:


function arrayOfHiNTimes(n) {
    let hiArray = []; 
    for (let i = 0; i < n; i++) {
        hiArray[i] = 'hi';
    }
    return hiArray;
}

console.log(arrayOfHiNTimes(6))

//what is the time complexity and space complexity for the second example:
// - Time complexity - O(n)
// - Space complexity - O(n)