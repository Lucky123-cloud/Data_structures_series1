// 1. Global context
console.log("1. Global context:", this); // In browser: window

// 2. Regular function
function regularFunction() {
  console.log("2. Regular function:", this); // In browser: window
}
regularFunction();

// 3. Method inside an object
const person = {
  name: "Lucky",
  greet: function () {
    console.log("3. Object method:", this.name); // Lucky
  }
};
person.greet();

// 4. Arrow function inside object
const arrowPerson = {
  name: "Alex",
  greet: () => {
    console.log("4. Arrow function in object:", this.name); // undefined (from global scope)
  }
};
arrowPerson.greet();

// 5. Constructor function
function Car(brand) {
  this.brand = brand;
  console.log("5. Constructor function:", this.brand); // e.g., Toyota
}
const myCar = new Car("Toyota");

// 6. call(), apply(), bind()
function showName() {
  console.log("6. With call/apply/bind:", this.name);
}

const user = { name: "Samantha" };
showName.call(user);      // Samantha
showName.apply(user);     // Samantha
const bound = showName.bind(user);
bound();                  // Samantha

// 7. Arrow function capturing outer 'this'
const outer = {
  name: "Outer",
  print: function () {
    const arrow = () => {
      console.log("7. Arrow capturing outer this:", this.name); // Outer
    };
    arrow();
  }
};
outer.print();
