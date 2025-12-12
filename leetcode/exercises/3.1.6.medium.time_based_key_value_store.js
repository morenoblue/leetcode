// -----------------------
// Created     : 11/12/2025
// Last Edited : 12/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 981. Time Based Key Value Store
// References  :
// Notes       :
// -----------------------

var TimeMap = function() {
    this.data = {};
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if (key in this.data) {
        this.data[key].push([value, timestamp]); 
    } else {
        this.data[key] = [[value, timestamp]];
    }
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {

    if (!(key in this.data)) return "";

    let l = 0;
    let r = this.data[key].length - 1;
    let res = "";
    while (l <= r) {
        let m = Math.floor(l + (r - l) / 2);

        if (this.data[key][m][1] == timestamp){
            return this.data[key][m][0]
        }

        if (this.data[key][m][1] < timestamp){
            res = this.data[key][m][0];
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    return res
};

