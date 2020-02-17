# 581 Shortest unsorted continuous subarray

## First attempt
```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0
        
        min_start = [0 for i, _ in enumerate(nums)]
        max_start = [0 for i, _ in enumerate(nums)]
        min_start[0] = max_start[0] = nums[0]
        for i in range(1, len(nums)):
            min_start[i] = (min(min_start[i-1], nums[i]))
            max_start[i] = (max(max_start[i-1], nums[i]))
        
        min_end = [0 for i, _ in enumerate(nums)]
        max_end = [0 for i, _ in enumerate(nums)]
        min_end[-1] = max_end[-1] = nums[-1]
        for i in reversed(range(0, len(nums) - 1)):
            min_end[i] = min(min_end[i+1], nums[i])
            max_end[i] = max(max_end[i+1], nums[i])
        
        for i in range(len(nums)):
            if max_start[i] > min_end[i]:
                break
        start = i
        for i in reversed(range(len(nums))):
            if min_end[i] < max_start[i]:
                break
        end = i
        
        return max(0, end - start + 1)
```

## Sort
We could also sort the array and compare the sorted array with the original array.

## Stack
Similar to the [daily temperatures](daily-temperatures.md) question.

## Keywords
Array
