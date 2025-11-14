/*
* @param {number[]} array
* @param {number} target
* @return {bool}
*/
var binary_search = function(array, target) {
    start = 0;
    end = array.length;
    while (start < end) {
        middle = Math.floor(start + (end - start)/2)
        if (array[middle] === target) { return true }

        if (array[middle] < target) { 
            start = middle + 1
        } else {
            end = middle
        }
    }
    return false
}

console.log(binary_search([1, 3, 11, 12, 14, 18, 18, 19], 19))
