// -----------------------
// Created     :8/11/2025
// Last Edited :8/11/2025 
// Topics      :
// Big O       :
// Problem Id  :0
// Source      :
// Notes       :
// -----------------------

var MinStack = function() {
    this.obj = [];
    this.minvals = [];
    
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {

    if (this.minvals.length == 0) {
        this.minvals.push(0);
    } else if (val < this.obj[this.minvals[this.minvals.length - 1]]) {
        this.minvals.push(this.obj.length);
    } else {
        this.minvals.push(this.minvals[this.minvals.length - 1]);
    }

    this.obj.push(val);

};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.obj.pop();
    this.minvals.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.obj[this.obj.length - 1]; 
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.obj[this.minvals[this.minvals.length - 1]];
};

var obj = new MinStack();
console.log(obj.push(0));
console.log(obj.push(1));
console.log(obj.push(0));
console.log(obj.getMin());
console.log(obj.pop());
console.log(obj.getMin());
console.log(obj.pop());
console.log(obj.getMin());
console.log(obj.pop());
console.log(obj.push(-2));
console.log(obj.push(-1));
console.log(obj.push(-2));
console.log(obj.getMin());
console.log(obj.pop());
console.log(obj.top());
console.log(obj.getMin());
console.log(obj.pop());
console.log(obj.getMin());
console.log(obj.pop());
