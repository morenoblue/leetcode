// -----------------------
// Created    : 07/11/2025
// Last Edited: 07/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 238
// -----------------------

/*
* @param {number[]} nums
* @return {number[]} 
*/
var productExceptSelf = function (nums) {

    res = Array.from({length: nums.length}, () => 1)

    prefix = 1
    for (let i = 0; i < nums.length; i++) { 
        res[i] = prefix
        prefix *= nums[i]
    }
    
    postfix = 1
    for (let i = nums.length - 1; i > 0; i--) {
    res[i-1] *= postfix*nums[i]
    postfix *= nums[i]
    }
    return res
}

console.log(productExceptSelf([1,2,3,4]))
