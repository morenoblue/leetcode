// -----------------------
// Created     : 28/11/2025
// Last Edited : 28/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 
// References  : 
// Notes       : Self Solved
// -----------------------


var searchMatrix = function(matrix, target)  {
    let t = 0;
    let b = matrix.length;
    let mr;
    while (t < b) {
        mr = Math.floor(t + (b - t) / 2)
        if (target >= matrix[mr][0] && target <= matrix[mr][matrix[mr].length - 1]) {
            break
        } else if (target < matrix[mr][0]) {
            b = mr;
        } else {
            t = mr + 1;
        }
        if (t >= b) {
            return false
        }
    }

    let l = 0;
    let r = matrix[0].length;
    let mc;
    while (l < r) {
        mc = Math.floor(l + (r - l) / 2)
        if (target == matrix[mr][mc]) {
            return true
        } else if (target < matrix[mr][mc]) {
            r = mc;
        } else {
            l = mc + 1;
        }
    }
    return false
}

console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60));
