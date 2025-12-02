// -----------------------
// Created     : 02/12/2025
// Last Edited : 02/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 
// References  : https://www.youtube.com/watch?v=U2SozAs9RzA
// Notes       : 
// -----------------------

/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let l = 1;
    let r = Math.max(...piles);
    let res = 0;
    while (l <= r) {
        k = Math.floor(l + (r - l) / 2)
        let s = 0;
        for (const p of piles) {
            s += Math.ceil(p/k);
        }

        if (s <= h) {
            res = k;
            r = k - 1;
        } else {
            l = k + 1;
        }

    }
    return res;
}

console.log(minEatingSpeed([1, 10, 2, 5, 4, 3], 10));
