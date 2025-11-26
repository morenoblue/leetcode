// -----------------------
// Created     : 26/11/2025
// Last Edited : 26/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 150
// References  :
// Notes       : Man this backtracking stuff is tuff
// -----------------------

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const stack = [];
    const res = [];
    var backtracking = function(open, close) {
        if (open === n && close === n) {
            res.push(stack.join(""));
            return
        }

        if (open < n) {
            stack.push("(");
            backtracking(open + 1, close);
            stack.pop();
        }

        if (close < open) {
            stack.push(")");
            backtracking(open, close + 1);
            stack.pop();
        }

    }
    backtracking(0, 0);
    return res
}

console.log(generateParenthesis(3));
