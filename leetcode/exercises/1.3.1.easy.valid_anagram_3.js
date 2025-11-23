// -----------------------
// Created     : 24/10/2025
// Last Edited : 24/10/2025
// Topics      : 
// Big O       : 
// Problem Id  : 242
// References  :
// Notes       :
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


