// -----------------------
// Created    : 13/11/2025
// Last Edited: 13/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 11
// -----------------------

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let l = 0;
    let r = height.length - 1;
    let max_height = 0;

    for (let i = 0; i < height.length; i++) {
        base = Math.abs(r - l); 
        h = Math.min(height[l], height[r]);
        max_height = Math.max(max_height, base*h)
        if (height[l] < height[r]) {
            l++;
        } else if (height[l] > height[r]) {
            r--;
        } else {
            l++;
            r--;
        }
    }
    return max_height;

};

console.log(maxArea([1,2,1]));


