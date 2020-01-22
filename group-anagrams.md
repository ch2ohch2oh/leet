# 49 Group anagrams

## Solution using a dictionary

One step further, one can use `set` as the key of a dictionary as shown [here](https://leetcode.com/problems/group-anagrams/solution/).

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            key = ''.join(sorted(list(s)))
            if key in seen.keys():
                seen[key].append(s)
            else:
                seen[key] = [s]
        return seen.values()
```

## Keywords
Hashtable
