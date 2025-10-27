// -----------------------
// Created       : 27/10/2025
// Last Edited   : 27/10/2025
// Big O         :
// Topics        : 
// Problem Id    : 347
// -----------------------

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const counts = {}
    for (num of nums)
    {
        counts[num] = (counts[num] ?? 0) + 1;
    };

    const frequency = Array.from({length: nums.length}, () => []);
    for (num of Object.keys(counts))
    {
        frequency[counts[num]-1].push(Number(num));
    };

    res = []
    for (let i = frequency.length-1; i >= 0; i--)
    {
        for (const j of frequency[i])
        {
            if (res.length !== k){
                res.push(j);
            };
        };
    };

    return res;
};

console.log(topKFrequent([1,1,2,2,3,3,3,5,6,5], 3));
