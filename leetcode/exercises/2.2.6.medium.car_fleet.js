// -----------------------
// Created     : 24/11/2025
// Last Edited : 24/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 853
// References  : https://www.youtube.com/watch?v=Pr6T-3yB9RM
// Notes       : 
// -----------------------

/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, positions, speeds) {
    const pairs = positions.map((pos, i) => [pos,speeds[i]]);
    pairs.sort((a, b) => b[0] - a[0]);

    const stack = [];
    for (const [position, speed] of pairs) {
        rs = (target - position) / speed;

        if (stack.length === 0 || rs > stack[stack.length - 1]) {
            stack.push(rs);
        }
    }
    return stack.length
};

console.log(carFleet(10, [8, 6], [3, 2]));
