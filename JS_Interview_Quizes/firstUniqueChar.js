// Write a function that takes in a string and returns the index of the
//  first non-repeating character. If it does not exist return -1.


function firstUniqueChar(str) {
    const charCount = {};
    //count the frequency of each character
    for(let char of str) {
        charCount[char] = (charCount[char] || 0) + 1;
    }

    //find the index of the first non-repeating character
    for(let i = 0; i<str.length; i++) {
        if (charCount[str[i]] === 1) {
            return i;
        }
    }

    return -1; //no unique character found
}

// Example test cases
console.log(firstUniqueChar("leetcode"));     // Output: 0
console.log(firstUniqueChar("loveleetcode")); // Output: 2
console.log(firstUniqueChar("aabbcc"));       // Output: -1
