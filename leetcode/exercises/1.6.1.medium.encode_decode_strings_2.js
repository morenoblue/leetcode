// -----------------------
// Created     : 28/10/2025
// Last Edited : 28/10/2025
// Topics      : 
// Big O       :
// Problem Id  : 271
// References  :
// Notes       :
// -----------------------

class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        var encoded = "";
        for (const str of strs)
        {
            encoded += str.length.toString() + "#" + str
        };
        return encoded;
    };

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        var i = 0;
        var str_len = "";
        var res = [];
        while (i < str.length)
        {
            if (str[i] != "#") { 
                str_len += str[i];
                i += 1;
            } else {
                res.push(str.slice(i+1, i+1+Number(str_len)));
                i = i+1+Number(str_len)
                str_len = "";
            };
        };
        return res;
    }
}

sol = new Solution();
console.log(sol.encode(["oi", "tudo", "bem?"]));
console.log(sol.decode(sol.encode(["oi", "tudo", "bem?"])));


