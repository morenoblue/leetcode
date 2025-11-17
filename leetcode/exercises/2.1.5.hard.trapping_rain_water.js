// -----------------------
// Created    : 17/11/2025
// Last Edited: 17/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 42
// -----------------------

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let res = 0;
    let l_m = 0;
    let r_m = 0;
    let l = 0;
    let r = height.length - 1;
    while (l <= r) {
        if (l_m <= r_m) {
            res += Math.max(l_m - height[l], 0);
            if (height[l] > l_m) {
                l_m = height[l];
            }
            l += 1;
        } else {
            res += Math.max(r_m - height[r], 0);
            if (height[r] > r_m) {
                r_m = height[r];
            }
            r -= 1;
        }
    }
    return res;
};

console.log(trap([4,2,0,3,2,5]))
