let user = {
    age: 45,
    name: 'Kyle',
    magic: true,
    scream: function() {
        console.log('aaaaaahhh');
    }
}

user.age //O(1);
user.spell = "abra kadabra"; //O(1);
user.scream(); //O(1);

// https://www.cs.usfca.edu/~galles/visualization/OpenHash.html - hashtables
// https://en.wikipedia.org/wiki/Hash_table 

//the only problem with objects is that you do not have an option of using something else as the key:
//it has be to only strings, there is no order as well in objects

//we can correct this by using Map() in JS
//maps allows as to use anything as key - not just string

const a = new Map();

//we can use also set()
//Set is also very similar to map, but it only stores the keys
const b = new Set();