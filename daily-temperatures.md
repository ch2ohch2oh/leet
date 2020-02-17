# 739 Daily temperatures

## Brute force (time limit exceeded)
This method will work but will exceed the time limit.

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = []
        for i in range(len(T)):
            ans.append(0)
            for j in range(i + 1, len(T)):
                if T[i] < T[j]:
                    ans[i] = j - i
                    break
        return ans
```

## Using stack
So what is the idea behind this method using stack?
Suppose we are given the temperaure today. If the temperature
of tomorrow is higher then we know we just need to wait for 
oen day. However, if the temperature tomorrow is lower,
we have to record it and look at the temperature of the day
after tomorrow. Once we encounter a day with high temperature,
we go back and check if any "unsolved days" could be solved.

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0 for i, _ in enumerate(T)]
        for i, _ in enumerate(T):
            if len(stack) > 0 and T[i] > T[stack[-1]]:
                while len(stack) > 0 and T[i] > T[stack[-1]]:
                    top = stack.pop()
                    ans[top] = i - top
            stack.append(i)
        return ans
```

## Keywords
stack
