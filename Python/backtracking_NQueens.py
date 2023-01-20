# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:23:46 2023

@author: USER
"""
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
# such that no two queens attack each other.
# N Queens: Example 1
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens’ placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

# temp = [[2, 4, 1, 3], [3, 1, 4, 2]]
# test = ['.', '.', '.', '.']
# test[2] = "Q"
# test
# ''.join(test)


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(A):
        import copy
        global result
        result = []
        def checking(board, r, c): 
            for i in range(c):
                if (board[r][i]):
                    return False
            i = r
            j = c
            while i >= 0 and j >= 0:
                if(board[i][j]):
                    return False
                i -= 1
                j -= 1 
            i = r
            j = c
            while j >= 0 and i < A:
                if(board[i][j]):
                    return False
                i = i + 1
                j = j - 1         
            return True
        def main(board, c):
            if (c == A):
                v = []
                for i in board:
                  for j in range(len(i)):
                    if i[j] == 1:
                      v.append(j+1)
                result.append(v)
                return True

            temp = False
            for i in range(A):
                if (checking(board, i, c)):
                    board[i][c] = 1
                    temp = main(board, c + 1) or temp
                    board[i][c] = 0  
            return temp
        board = [[0 for j in range(A)] for i in range(A)]
        main(board, 0)
        # print(result)
        result.sort()
        board2 = [['.' for j in range(A)] for i in range(A)]
        result2 =[]
        # print(len(result))
        for i in range(len(result)):
            result2.append(copy.deepcopy(board2))
            for j in range(A):
                temp = ''
                # print(i, j, result[i][j])
                c_ix = result[i][j] - 1
                # print(c_ix, i, j)
                # print(result2[i][j])
                # print(result2[i])
                result2[i][j][c_ix] = 'Q'
                result2[i][j] = temp.join(result2[i][j])
            # print(result2[i])
            # print(result2)
        return result2
        # return result
A = 1
A = 2 
A = 3
A = 4
A = 5
solveNQueens(A)
 
# Editorial:
#     class Solution:
#     # @param A : integer
#     # @return a list of list of strings
#     def solveNQueens(self, A):
#         n=A
#         stack, res = [[(0, i)] for i in range(n)], []
#         while stack:
#             board = stack.pop()
#             row = len(board)
#             if row == n:
#                 res.append([''.join('Q' if i == c else '.' for i in range(n))
#                             for r, c in board])
#             for col in range(n):
#                 if all(col != c and abs(row-r) != abs(col-c)for r, c in board):
#                     stack.append(board+[(row, col)])
#         return res
#     class Solution {
# public:
#     vector<vector<string> > solveNQueens(int n) {
#         vector<vector<string> > solution;
#         vector<int> arr(n);
#         solveNQueensImpl(0, arr, solution);
#         return solutions;
#     }
    
#     void solveNQueensImpl(int col, vector<int> &arr, vector<vector<string> > &solution) {
#         int n = solution.size();
#         if (col == n) {
#             solution.push_back(solToStrings(arr));
#             return;
#         }
#         // For each row...
#         for (int row = 0; row < n; ++row) {
#             // Skip if there is another queen in this column or diagonals
#             if (isAvailable(arr, col, row)) {
#                 solution[col] = j;
#                 solveNQueensImpl(col + 1, arr, solution);
#             }
#         }
#     }

#     bool isAvailable(const vector<int> &arr, int col, int row) {
#         for (int prev_col = 0; prev_col < col; ++prev_col) {
#             if (row == arr[prev_col] ||  col + row == prev_col + arr[prev_col] || col - row == prev_col - arr[prev_col]) return false;
#         }
#         return true;
#     }

#     vector<string> solToStrings(const vector<int>& sol) {
#         int n = sol.size();
#         vector<string> sol_strings(n);
#         for (int i = 0; i < n; ++i) {
#             sol_strings[i] = string(n, '.');
#             sol_strings[i][sol[i]] = 'Q';
#         }
#         return sol_strings;
#     }
# };