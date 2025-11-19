// -----------------------
// Created    : 19/11/2025
// Last Edited: 19/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 150
// -----------------------

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    stack = [];
    let a = 0;
    let b = 0;
    for (const v of tokens) {
        if (v === "+") {

            stack.push(stack.pop() + stack.pop());

        } else if ( v === "-") {

            a = stack.pop();
            b = stack.pop();
            stack.push(b - a);

        } else if (v === "/") {

            a = stack.pop();
            b = stack.pop();
            stack.push(Math.trunc(b / a));

        } else if (v === "*") {
            stack.push(stack.pop() * stack.pop());

        } else {
            stack.push(Number(v));
        }
    }
    return stack[0];
    
};

console.log(evalRPN(["4","13","5","/","+"]));
