# 930 Binary subarrays with sum

## Prefix sum
This problem took me quite a bit of time even 
after I took a look at the solution. 
Must be careful about where to put the update line!

```python
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = defaultdict(int)
        current = 0 # current sum
        ans = 0
        for num in A:
            current += num
            if current == S:
                ans += 1
            ans += count[current - S]
            # have to put this line at last!!!
            count[current] += 1
            # print(f'num = {num} count = {count} ans = {ans}')
        return ans
```

## Keywords
Prefix sum
