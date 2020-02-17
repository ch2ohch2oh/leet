# 448 Find all numbers disappeared in an array

## Naive method using extra space

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = [0 for i in range(len(nums) + 1)]
        for num in nums:
            seen[num] += 1
        not_seen = []
        for i in range(1, len(seen)):
            if seen[i] == 0:
                not_seen.append(i)
        return not_seen
```
## Iteration without extra space
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # mark all found number as 0
            if nums[i] == 0:
                continue
            else:
                num = nums[i]
                while nums[num - 1] != 0:
                    new_num = nums[num - 1]
                    nums[num - 1] = 0 
                    num = new_num
            # print(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(i + 1)
        return ans
```

## Keywords
Array
