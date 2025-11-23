// -----------------------
// Created     : 23/10/2025
// Last Edited : 23/10/2025
// Topics      : 
// Big O       :
// Problem Id  : 217
// References  :
// Notes       :
// -----------------------

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) 
{
    nums.sort();

    for (let i = 1; i < nums.length; i++)
    {
        if (nums[i-1] === nums[i]){ return true };
    };
    return false;
};

console.log(containsDuplicate([1, 2, 3, 10, 8, 1]))

