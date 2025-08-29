//here we will get the understanding of O(1)
//here we do it in a way that makes it good and possible to work at constant time.
// The O(1) is called constant time, because nothing changes. lets see the example:

const boxes = [1, 2, 3, 4, 5, 6];
function compressOnlyOneBox(boxes){
    console.log(boxes[0]);
}

compressOnlyOneBox(boxes)
//This will only compress only one box and return one box even though the boxes are as much as 6 boxes.
//hence it is called O(1). Look at the bigO_image.png to see its perfomance, it is the best.

//if we had, more then that means, we woould have done the same thing.
//here the function only returns the first 3 boxes, we except it to be O(3). However, we still term it as O(1) as it is constant
const boxes2 = [1, 2, 3, 4, 5, 6];
function compressOnlyOneBox2(boxes){
    console.log(boxes[0]);
    console.log(boxes[1]);
    console.log(boxes[2]);
}

compressOnlyOneBox2(boxes2)
