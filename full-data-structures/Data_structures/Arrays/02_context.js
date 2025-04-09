//what is the difference between a scope and context
//As soon as we create a new function, there is always a scope, hence a scope is created when a new function is created
function b() {
    let a = 4;
}
// console.log(a) - this will say that 'a' is not defined

//context - tells you where we are within the object
const object4 = {
    a: function() {
        console.log(this);
    }
}

//instantiation
class Player {
    constructor(name, type) {
        console.log('Player', this);
        this.name = name;
        this.type = type;
    }
    introduce() {
        console.log(`Hi I am ${this.name} I'm a ${this.type}`)
    }
} 

class Wizard extends Player {
    constructor(name, type) {
        super(name, type)
        console.log('wizard', this);
    }
    play() {
        console.log(`Weeeeeeeee I'm a ${this.type}`)
    }
}

const wizard1 = new Wizard('Shelly', 'Healer');
const wizard2 = new Wizard('Shawn', 'Dark Magic');