# 221 Maximal square

## Brute force search

Still the corner case of empty input list is annoying.

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        row_size = len(matrix)
        col_size = len(matrix[0])
        ans = 0
        for i in range(row_size):
            for j in range(col_size):
                ans = max(ans, self.find_max(matrix, i, j))
                # print(f'({i}, {j}) => {ans}')
        return ans
    
    def find_max(self, matrix, row, col):
        if matrix[row][col] == '0':
            return 0
        row_size = len(matrix)
        col_size = len(matrix[0])
        size = 1
        fail = False
        while True:
            if row + size >= row_size or col + size >= col_size:
                break
            for i in range(row, row + size + 1):
                if matrix[i][col + size] == '0':
                    fail = True
                    break
            for i in range(col, col + size + 1):
                if matrix[row + size][i] == '0':
                    fail = True
                    break
            if not fail:
                size += 1
            else:
                break
        return size ** 2
```

## DP

The wrong way to create a two dimensional array in python is 
```python
>>> a = [[0] * 3] * 3
>>> a
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> a[0][0] = 233
>>> a
[[233, 0, 0], [233, 0, 0], [233, 0, 0]]
```

Never expected something like this could happen for a python list.

```python
import copy

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == [] or matrix == [[]]:
            return 0
        row_size = len(matrix)
        col_size = len(matrix[0])
        # Create a 2d array fille with zeros
        ans = [[0 for i in range(col_size)] for j in range(row_size)]
        best = 0 
        for i in range(row_size):
            for j in range(col_size):
                if i == 0 or j == 0:
                    ans[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    ans[i][j] = min(ans[i - 1][j], min(ans[i][j - 1], ans[i - 1][j - 1])) + 1
                    # print(f'{i} {j} => {ans[i][j]}')
                else:
                    ans[i][j] = 0
                
                best = max(best, ans[i][j])
        return best ** 2
```

## Keywords
DP