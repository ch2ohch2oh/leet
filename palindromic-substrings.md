# 647 Palindromic substrings

## Brute force (TLE)
This method will exceed the time limit.

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        ans = 0
        for i in range(size):
            for j in range(i, size):
                sub = s[i:j+1]
                fail = False
                for k in range(len(sub) // 2 + 1):
                    if sub[k] != sub[len(sub) - k -1]:
                        fail = True
                        break
                if not fail:
                    ans += 1
        return ans
```

## DP
This seems to be a overkill and is not significantly faster.

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        ans = 0
        palin = [[0 for i in range(size)] for j in range(size)]
        
        # substring of length 1 is palindromic
        for i in range(size):
            palin[i][i] = 1
            ans += 1
        
        for sublen in range(2, size + 1):
            for start in range(0, size - sublen + 1):
                end = start + sublen - 1
                
                if s[start] == s[end] and sublen == 2:
                    palin[start][end] = 1
                    ans += 1
                elif s[start] == s[end] and palin[start + 1][end - 1] == 1:
                    palin[start][end] = 1
                    ans += 1
                # print(f'{start} to {end} ans = {ans}')
        # print(palin)
        return ans
```

## Expand around center
This should be natural to come to mind but I did not 
think about this method at all. The solution is 
[here](https://leetcode.com/problems/palindromic-substrings/solution/).

## Keywords
string
