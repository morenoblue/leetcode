// -----------------------
// Created    : 08/11/2025
// Last Edited: 08/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 238
// -----------------------

/*
* @param {number[]} nums
* @return {number}
*/
var longestConsecutive = function(nums) {
        const unique_nums = new Set(nums)

        let max_seq_size = 0
        let curr_seq_size;
        for (const num of unique_nums) {
            if (!unique_nums.has(num-1)) {
                curr_seq_size = 1 
                while (unique_nums.has(num+curr_seq_size)) {
                    curr_seq_size += 1
                }
                max_seq_size = Math.max(max_seq_size, curr_seq_size)
            }
        }

        return max_seq_size
}

console.log(longestConsecutive([100,4,200,1,3,2]))
