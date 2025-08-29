// Debouncing is a performance optimization technique that ensures a function is 
// executed only after a specified delay following the last event. It’s particularly
//  useful for handling rapid, repetitive events such as user input, scrolling,
// or window resizing, preventing unnecessary function calls and improving efficiency.

//using debounce with lodash

import { debounce } from 'lodash';

const searchInput = document.getElementById('search-input');

const debouncedSearch = debounce(() => {
    //perform the search operations here
    console.log('seaching for: ', searchInput.value);
}, 300)

searchInput.addEventListener('input', debouncedSearch);


//custom debounce without Lodash

function debounce2(fn, delay) {
    let timer;
    return function (...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
    };
}

//usage
const handleInput = debounce2(() => {
    console.log('Custom debounce:', searchInput.value);
}, 300);

searchInput.addEventListener('input', handleInput);