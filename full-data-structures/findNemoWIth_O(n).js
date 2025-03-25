// This is O(n)
//this is the big o notation calculation:

//If we have a function called findNemo, how to we know that this code can scale(Big O notation measuring):
const name = ['Nemo']
const large = new Array(10000).fill('Nemo');
function findNemo(arr) {
    const t0 = performance.now();
    for(let i = 0; i < arr.length; i++) {
        if (arr[i] === 'Nemo') {
            console.log("Found Nemo");
        } else {
            console.log('We did not find Nemo');
        }
    }
    const t1 = performance.now();
    console.log(`The time taken to find Nemo is ${t1-t0} milliseconds`); 
}

findNemo(large);


//so what do we notice here, as the input increases, we also have an increase in time taken to get Nemo.
// Well it is not time that increases, because we have said that time is not a factor, so we use the factor of 
// number of operations that need to work on the input. 
//this is big O called O(n). Refer to the image bigO_image.png to see. This is called Linear time. 