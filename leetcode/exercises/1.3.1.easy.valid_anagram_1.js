// -----------------------
// Created     : 24/10/2025
// Last Edited : 24/10/2025
// Topics      : 
// Big O       :
// Problem Id  : 242
// Source      :
// Notes       :
// -----------------------

// note(@morenoblue): This solution isn't finished. I have no idea how to 
//                    reliably compare two objects in javascript without 
//                    importing a library. But its just a matter of comparing 
//                    the two objects in the end to check if they are the same, 
//                    which if they are, then the strings are indeed anagrams.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) { return false };

    s_counter = {};
    t_counter = {};

    for (let i = 0; i < s.length; i++)
    {
       s_counter[s[i]] = (s_counter[s[i]] ?? 0) + 1 
       t_counter[t[i]] = (t_counter[t[i]] ?? 0) + 1 
    };

};
