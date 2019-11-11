# 29 Divide two integers - Medium
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = - 2 ** 31
        int_max = 2 ** 31 - 1
        # dividend  = divisor * answer + remainder
        # answer => bit representation
        
        # The divisor and the dividend could be negative
        if dividend == 0:
            return 0
        sign = 1 if dividend * divisor > 0 else -1
        up = abs(dividend)
        down = abs(divisor)
        if up == down:
            return sign
        # Find the max
        factor = 1
        ans = 0
        # Take extra care at the decision boundary. 
        # Think well whether it should be >= or >
        while up >= down * factor:
            factor <<= 1
            # print('factor', factor)
        factor >>= 1
        ans += factor
        # print('ans', ans , 'factor', factor)
        up -= down * factor
        # Go down
        while factor > 1:
            factor >>= 1
            if up >= down * factor:
                ans += factor
                up -= down * factor
            # print('ans', ans)
        ans = ans * sign
        # Handle overflow and underflow
        if ans < int_min:
            return int_min
        elif ans > int_max:
            return int_max
        else:
            return ans
