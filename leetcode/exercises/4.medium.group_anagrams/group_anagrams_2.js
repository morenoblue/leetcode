// -----------------------
// Created       : 25/10/2025
// Last Edited   : 25/10/2025
// Big O         :
// Topics        : 
// Problem Id    : 49
// -----------------------

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    map = {}; 
    for (const str of strs)
    {
        const key = Array(26).fill(0);
        for (const char of str)
        {
            key[char.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        };
        (map[key] ?? (map[key] = [])).push(str); 
    };
    return Object.values(map);
};

console.log(groupAnagrams(["oi", "tchau", "io", "tui", "itu"]));
