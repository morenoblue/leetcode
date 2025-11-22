// -----------------------
// Created     :7/11/2025
// Last Edited :7/11/2025 
// Topics      :
// Big O       :
// Problem Id  :38
// Source      :
// Notes       :
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
