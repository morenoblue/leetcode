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
    if (s.length !== t.length) { return false };

    counter = {};
    for (let i = 0; i < s.length; i++)
    {
       counter[s[i]] = (counter[s[i]] ?? 0) + 1 
       counter[t[i]] = (counter[t[i]] ?? 0) - 1 
    };
    
    for (const k in counter) { if (counter[k] !== 0) return false};
    return true
};

