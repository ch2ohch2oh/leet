# 26 Remove duplicates from sorted array

## Use two pointers
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return left + 1
```

## Keywords 
Two pointers