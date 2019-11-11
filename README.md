#  Leet :)
## Bitwise operations
- 29 Divide Two Integers (Medium) 

  Should have tested throughly before submission. Think carefully about whether
  `>` or `>=` should be used at the decision boundary.

- Another

## Two pointers
- 880 Decoded String at Index (Medium)

  My solution is to use two pointers and recursion. This is not optimal.
  [A better solution](https://leetcode.com/problems/decoded-string-at-index/discuss/354312/Python-Simple-Intuitive-Solution) 
  is to decode the string to be longer than `K`. Then go 
  backwards to find what is the `K-th` character. Again comprehensive testing
  is needed before the submission.
  
## String manipulation
- 306 Additive Number (Medium)

  The leading zeros require extra care. Spent tons of time to debug only to 
  find out I modified a variable inside inner loop by mistake :-(. 
  I tried to optimize the range of loop but did it wrong at first. 
  Lesson learnt: do NOT optimize too early.

