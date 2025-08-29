//Google Question
//Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4];
//it should return 2

//given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
//it should return 1

//Given an array = [2, 3, 4, 5]
//it should return undefined

function firstRecuringCharacter(input) {
    for (let i = 0; i < input.length; i++) {
        for (let j = i + 1; j < input.length; j++) {
            if(input[i] === input[j]) {
                return input[i];
            }
        }
    }
    return undefined;
} //O(n*2)


//second and better implementation using hash Tables
//O(n)
function firstRecuringCharacter2(input) {
   let map = {};
   for(let i = 0; i <input.length; i++) {
    if(map[input[i]]) {
        return input[i]
    } else {
        map[input[i]] = i
    }
    console.log(map);
   }
  
   return undefined;
} //O(n)


console.log(firstRecuringCharacter([3, 1, 2, 1, 3, 4, 5, 1, 2]))