// -----------------------
// Created     : 24/10/2025
// Last Edited : 24/10/2025
// Topics      : 
// Big O       :
// Problem Id  : 1
// Source      :
// Notes       :
// -----------------------

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = {};
    for (const [i, value] of nums.entries())
    {
        const complement = target - value;
        if (complement in map) { return [map[complement], i] };
        map[value] = i;
    };
};

console.log(twoSum([1, 2, 3, 10, 4, 8, 7], 12))
