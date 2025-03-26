// What is the Big O of the below function? (Hint, you may want to go line by line)
function funChallenge(input) {
    let a = 10;  //O(1)
    a = 50 + 3; //O(1)
  
    for (let i = 0; i < input.length; i++) { // O(n)
      anotherFunction(); //O(n)
      let stranger = true; //O(n)
      a++; // O(n)
    }
    return a; //O(1)
  }

//lets add it up, we have 3(1) and 4(n)
//that is the same as O(3 + 4n): our code is a Big O(3 + 4n)
//later we will realise that this is just O(n).
