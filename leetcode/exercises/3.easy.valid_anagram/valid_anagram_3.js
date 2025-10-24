// -----------------------
// Created       : 24/10/2025
// Last Edited   : 24/10/2025
// Big O         : 
// Topics        : 
// Problem Id    : 242
// -----------------------

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    return s.split("").sort().join("") === t.split("").sort().join("");
};

console.log(isAnagram("economia", "enocomia"));


