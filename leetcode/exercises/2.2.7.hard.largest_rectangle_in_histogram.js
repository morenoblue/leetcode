// -----------------------
// Created     : 14/12/2025 
// Last Edited : 14/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 84
// References  : https://www.youtube.com/watch?v=zx5Sw9130L0
// Notes       : 
// -----------------------

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let stack = [];
    let max_area = 0;
    for (let i=0; i < heights.length + 1; i++) {

        if (i < heights.length) {
            var h = heights[i];
        } else {
            var h = 0;
        }

        if (stack.length === 0) {
            stack.push([i, h]);
            continue;
        }

        if (stack[stack.length-1][1] <= h) {
            stack.push([i, h]);
        } else {
            while (stack.length > 0 && h < stack[stack.length-1][1]) {
                let area = stack[stack.length-1][1] * (i - stack[stack.length-1][0]);
                max_area = Math.max(max_area, area);
                var start = stack[stack.length-1][0];
                stack.pop();
            }
            stack.push([start, h]);
        }
    }
    return max_area;
};
