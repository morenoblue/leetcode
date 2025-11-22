// -----------------------
// Created     :3/11/2025
// Last Edited :3/11/2025 
// Topics      :
// Big O       :
// Problem Id  :25
// Source      :
// Notes       :
// -----------------------

/*
* @param {string} s
* @return {boolean}
*/
var isPalindrome = function (s) {

    // function isalnum(s) {
    //     return /^[A-Za-z0-9]+$/.test(s)
    // }

    function isalnum(c) {
        const code = c.charCodeAt()
        return (
            (97 <= code && code <= 122) ||
            (65 <= code && code <= 90) ||
            (48 <= code && code <= 57)
        )
    }

    l = 0;
    r = s.length - 1;
    while (l < r) {
        while (!isalnum(s[l])) {
            l++;
            if (l == s.length) { return true }
        }
        while (!isalnum(s[r])) {
            r--;
        }
        if (s[l].toLowerCase() != s[r].toLowerCase()) { return false }
        l++;
        r--;
    }
    return true
}

console.log(isPalindrome("A man, a plan, a canal: Panama"))
