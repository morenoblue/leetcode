// -----------------------
// Created     : 02/12/2025
// Last Edited : 02/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 153. Find Minimum in Rotated Sorted Array
// References  : My brain 😏
// Notes       : Self Solved. I so proud rn. This is my first exercise that I 
//               solve by myself with the solution actually being optimal! I 
//               thought about the solution in the shower.
// -----------------------

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let l = 0; 
    let r = nums.length - 1;
    while (l <= r) {
        let m = Math.floor(l + (r - l) / 2);
        if (nums[l] < nums[r]) { return nums[l] }

        if (nums[l] <= nums[m]) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return nums[r];
}

console.log(findMin([4,5,6,7,1,2]))
