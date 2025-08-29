function *greet() {
    yield "Hello there",
    yield "How are you",
    yield "Goodbye"
}

let greeter = greet();

console.log(greeter.next().value)
console.log(greeter.next().value)
console.log(greeter.next().value)

function *asyncCode() {
    const data = yield fetchData() //pretend this is an asynchrounous code
    console.log(data);
}

// Use generators in ES6 when:

// You want to pause and resume a function manually (yield).

// You want to control asynchronous flow outside of the function.

// You want to implement lazy loading of data.

// You need to build iterators or custom data streams.