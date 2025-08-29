let wm = new WeakMap();

let obj = {};

wm.set(obj, "Secret name");

let ans = wm.get(obj)

console.log(ans)

//why use weakmaps 
//1. Private Data in classes

const privateData = new WeakMap();

class User {
    constructor(name) {
        privateData.set(this, { name });
    }

    getName() {
        return privateData.get(this).name;
    }
}

const u1 = new User("Lucky");
console.log(u1.getName());

//2. Automatic garbage collection

let obj1 = {};
const weakMap = new WeakMap();

weakMap.set(obj1, "data");

obj1 = null; //object is now unreachable

//at some point, JS garbage collector removes obj1 and its weakMap entry