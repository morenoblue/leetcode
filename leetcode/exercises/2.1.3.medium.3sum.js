// -----------------------
// Created     :3/11/2025
// Last Edited :3/11/2025 
// Topics      :
// Big O       :
// Problem Id  :5  
// Source      :
// Notes       :
// -----------------------

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {

    nums.sort((a,b) => a - b)
    const triplets = []

    for (let i = 0; i < nums.length; i ++) {
        if (i > 0 && nums[i] == nums[i-1]) { continue }

        let l = i + 1;
        let r = nums.length - 1;
        let sum = 0;

        while (l < r) {
            sum = nums[i] + nums[l] + nums[r]
            if (sum < 0) {
                l++
            } else if (sum > 0 ) {
                r--
            } else {
                triplets.push([nums[i], nums[l], nums[r]])

                l++
                while (l < r && nums[l] == nums[l-1]) {
                    l++
                }

                // note(@morenoblue): we could comment this code paragraph 
                //                    and it would still work.
                r--
                while (l < r && nums[r] == nums[r+1]) {
                    r--
                }
            }
        }
    }
    return triplets
};

console.log(threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
