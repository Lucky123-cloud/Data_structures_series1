function lengthOfLastWord(str) {
    // Trim trailing spaces and split by spaces
    const words = str.trim().split(" ");
    // Return length of the last word
    return words[words.length - 1].length;
  }
  
  // Example usage:
  console.log(lengthOfLastWord("Hello World")); // Output: 5
  console.log(lengthOfLastWord("   I am coding in JS   ")); // Output: 2