// -----------------------
// Created     : 18/12/2025
// Last Edited : 18/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 121. Best Time to Buy and Sell Stock
// References  : https://www.youtube.com/watch?v=1pkOgXD63yU
// Notes       :
// -----------------------

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let l = 0;
    let r = 1;
    let m = 0;
    while (r < prices.length) {
        profit = prices[r] - prices[l];
        if (profit < 0) {
            l = r;
            r += 1;
        } else {
            m = Math.max(m, profit);
            r += 1;
        }
    }
    return m  
};

console.log(maxProfit([7,1,5,3,6,4]));
