//we are always repeating newNode in the former code, 
//lets correct that... we will create a class through OOP for node:


class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }
        this.tail = this.head;
        this.length = 1;
    }
    append(value) {
        const newNode = new Node(value);
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++
        return this;
    }

    //adding to the begining of the list
    prepend(value) {
       const newNode = new Node(value)
        newNode.next = this.head;
        this.head = newNode;
        this.length++;
        return this
    }
}

const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(15);
console.log(myLinkedList);