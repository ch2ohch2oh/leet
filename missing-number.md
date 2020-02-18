# 268 Missing number

## Math
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxn = len(nums)
        total = sum(nums)
        return (maxn + 1) * maxn // 2 - total
```
## Keywords
Math