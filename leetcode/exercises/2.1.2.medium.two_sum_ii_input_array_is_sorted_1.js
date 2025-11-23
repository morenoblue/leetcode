// -----------------------
// Created     :3/11/2025
// Last Edited :3/11/2025 
// Topics      :
// Big O       :
// Problem Id  :67
// References  :
// Notes       :
// -----------------------

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    l = 0;
    r = numbers.length - 1;

    while (l < r) {
        let sum = numbers[l] + numbers[r];
        if (sum === target) { return [l+1, r+1]; } 
        if (sum < target) {
            l++;
        } else {
            r--;
        }
    }
    return [0, 0];
};

console.log(twoSum([2,7,11,15],13))
