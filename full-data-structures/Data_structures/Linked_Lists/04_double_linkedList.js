//implement a node class

class Node {
    constructor(value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}


//create a doublyLinkedList class
class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    //add a node to the end
    append(value) {
        const newNode = new Node(value);
        if (!this.head) {
            this.head = this.tail = newNode;
        } else {
            this.head.tail = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++;
    }
}