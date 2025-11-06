// -----------------------
// Created    : 06/11/2025
// Last Edited: 06/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 36
// -----------------------

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const cols   = Array.from({length: 9}, () => new Set());
    const rows   = Array.from({length: 9}, () => new Set());
    const blocks = Array.from({length: 9}, () => new Set());

    for (let r = 0; r < 9; r++) {

        for (let c = 0; c < 9; c++) {

            if (board[r][c] == ".") { continue }
            if (cols[c].has(board[r][c])) { return false; }
            if (rows[r].has(board[r][c])) { return false; } 
            if (blocks[Math.floor(r / 3)*3 + Math.floor(c / 3)].has(board[r][c])) { return false; }

            rows[r].add(board[r][c]);
            cols[c].add(board[r][c]);
            blocks[Math.floor(r / 3)*3 + Math.floor(c / 3)].add(board[r][c]);
        }
    }
    return true

};

console.log(isValidSudoku([["5","3",".",   ".","7",".",   ".",".","."]
                          ,["6",".",".",   "1","9","5",   ".",".","."]
                          ,[".","9","8",   ".",".",".",   ".","6","."]

                          ,["8",".",".",   ".","6",".",   ".",".","3"]
                          ,["4",".",".",   "8",".","3",   ".",".","1"]
                          ,["7",".",".",   ".","2",".",   ".",".","6"]

                          ,[".","6",".",   ".",".",".",   "2","8","."]
                          ,[".",".",".",   "4","1","9",   ".",".","5"]
                          ,[".",".",".",   ".","8",".",   ".","7","9"]]))

