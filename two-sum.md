# 1 Two sum

## Brute force

A two-level loop.
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
```

## Hash table

Memorize all the numbers we have seen.
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lastseen = dict()
        for i in range(len(nums)):
            other = target - nums[i]
            if other in lastseen.keys():
                return [lastseen[other], i]
            lastseen[nums[i]] = i
        return None
```

## Keywords
Hash table
