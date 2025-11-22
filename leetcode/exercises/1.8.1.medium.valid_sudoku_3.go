// -----------------------
// Created     :6/11/2025
// Last Edited :6/11/2025 
// Topics      :
// Big O       :
// Problem Id  :6
// Source      :
// Notes       :
// -----------------------

package main

import (
    "fmt"
)

func isValidSudoku(board [][]byte) bool {
    rows   := make([]map[byte]struct{}, 9)
    cols   := make([]map[byte]struct{}, 9)
    blocks := make([]map[byte]struct{}, 9)
    for i := 0; i < len(rows); i++ {
        rows[i]   = make(map[byte]struct{})
        cols[i]   = make(map[byte]struct{})
        blocks[i] = make(map[byte]struct{})
    }

    for r := 0; r < 9; r++ {

        for c := 0; c < 9; c++ {
            if board[r][c] == '.' { continue }
            if _, ok := rows[r][board[r][c]]; ok { return false }
            if _, ok := cols[c][board[r][c]]; ok { return false }
            if _, ok := blocks[(r / 3)*3 + (c / 3)][board[r][c]]; ok { return false }
            rows[r][board[r][c]] = struct{}{}
            cols[c][board[r][c]] = struct{}{} 
            blocks[(r / 3)*3 + (c / 3)][board[r][c]] = struct{}{}

        }

    }
    return true
}

func main () {

    fmt.Println(isValidSudoku([][]byte{
        {'8','3','.',   '.','7','.',   '.','.','.'},
        {'6','.','.',   '1','9','5',   '.','.','.'},
        {'.','9','.',   '.','.','.',   '.','6','.'},

        {'.','.','.',   '.','6','.',   '.','.','3'},
        {'4','.','.',   '8','.','3',   '.','.','1'},
        {'7','.','.',   '.','2','.',   '.','.','6'},

        {'.','6','.',   '.','.','.',   '2','8','.'},
        {'.','.','.',   '4','1','9',   '.','.','5'},
        {'.','.','.',   '.','8','.',   '.','7','9'},
    }))

}
