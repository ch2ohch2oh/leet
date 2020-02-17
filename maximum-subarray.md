# 53 Maximum subarray

## DP
The solution using DP and two pointers are almost 
identical. However, it is easier to prove that
our solution is finding the CORRET answer 
using DP.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current_sum is the max sum we can have ending at current position
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum
```

## Keywords
DP
