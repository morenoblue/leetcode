// -----------------------
// Created       : 24/10/2025
// Last Edited   : 24/10/2025
// Big O         :
// Topics        : 
// Problem Id    : 217
// -----------------------

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const counts = {};
    for (const n of nums){
        counts[n] = (counts[n] ?? 0) + 1;
        if (counts[n] > 1){ return true; };
    };
    return false
};

console.log(containsDuplicate([1, 2, 3, 10, 8]))

