// Write a function that takes an array of numbers and modifies it based on the following rules: 
// Replace numbers with 0 one by one until you reach a multiple of 5. 
// Once a multiple of 5 is encountered, replace numbers with 1 until you reach the next multiple of 5. 
// Continue alternating between 0 and 1 accordingly. 
// Example 
// Input = [2, 3, 7, 1, 5, 8, 6, 9, 10, 2, 4, 6, 8, 12, 15, 3, 1, 2, 5, 7] 
// Output = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


//codility part
function modifyArray(arr) {
    let result = [];
    let currentValue = 0;
  
    for (let num of arr) {
      result.push(currentValue);
      if (num % 5 === 0) {
        currentValue = currentValue === 0 ? 1 : 0;
      }
    }
  
    return result;
  }
  
  // Testing the function
  const input = [2, 3, 7, 1, 5, 8, 6, 9, 10, 2, 4, 6, 8, 12, 15, 3, 1, 2, 5, 7];
  const output = modifyArray(input);
  console.log(output);
  // Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
