// -----------------------
// Created     : 17/12/2025
// Last Edited : 18/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 4. Median of Two Sorted Arrays
// References  : https://youtu.be/q6IEA26hvXc?si=_FV_HNLEili4HEvg
// Notes       : This solution broke my spirit
// -----------------------

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let a = nums1;
    let b = nums2;
    if (nums1.length > nums2.length) {
        a = nums2;
        b = nums1;
    }
    
    let half = Math.floor((a.length + b.length) / 2);

    let l = 0;
    let r = a.length - 1;
    while (true) {
        let m_1 = Math.floor(l + (r - l) / 2);
        let m_2 = (half - (m_1 + 1)) - 1;

        let amax = m_1 >= 0 ? a[m_1] : -Infinity; 
        let bmax = m_2 >= 0 ? b[m_2] : -Infinity; 

        let amin = m_1 + 1 < a.length ? a[m_1 + 1] : Infinity; 
        let bmin = m_2 + 1 < b.length ? b[m_2 + 1] : Infinity; 

        if ((amax <= bmin) && (bmax <= amin)) {
            if (((a.length + b.length) % 2) != 0 ) {
                return Math.min(amin, bmin);
            }
            return (Math.max(amax, bmax) + Math.min(amin, bmin)) / 2;
        } else if (amax > bmin) {
            r = m_1 - 1;
        } else {
            l = m_1 + 1;
        }
    }
    
};

console.log(findMedianSortedArrays([1,2],[3,4]));
