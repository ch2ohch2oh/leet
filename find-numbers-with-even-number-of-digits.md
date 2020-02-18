# 1295 Find numbers with even number of digits

## Use log function
Take the log with base 10 to find the number of digits.
```python
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if math.floor(math.log10(num) + 1) % 2 == 0:
                count +=1
        return count
```

## Keywords
Math