// -----------------------
// Created    : 
// Last Edited: 
// Topics     : 
// Big O      :
// Problem Id : 20
// -----------------------

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    map = {
        "}":"{",
        ")":"(",
        "]":"[",
    };

    stack = [];
    for (const i of s) {
        if (i in map) {
            if (
                (stack.length == 0) ||
                (stack[stack.length - 1] != map[i])
            ) {
                return false;
            }
            stack.pop();
        } else {
            stack.push(i);
        }
    }

    if (stack.length == 0) { return true } 
    return false

};

console.log(isValid("(){}}{"))
