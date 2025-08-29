// Write a function that takes in an integer x and returns True if x is a palindrome
//  and False otherwise.


function isPalindrome(number) {
    if (x < 0) return false; // Negative numbers can't be palindromes
  
    const str = number.toString();
    const reversed = str.split('').reverse().join('');
  
    return str === reversed;
  }
  
  // Example test cases
  console.log(isPalindrome(121));    // Output: true
  console.log(isPalindrome(-121));   // Output: false
  console.log(isPalindrome(12321));  // Output: true
  console.log(isPalindrome(10));     // Output: false
  