class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # Since the length of the number is small
        # We can use a naive brute force method
        if len(num) < 3:
            return False
        for i in range(1, len(num)//2 + 1):
            # The first number can be a single 0
            if num[0] == '0' and i > 1:
                break
            first = int(num[:i])
            # print('first', first)
            for j in range(i + 1, len(num)):
                # The second number cannot have leading zero
                # unless it is just one single zero
                if num[i] == '0' and j > i + 1:
                    break
                if j - i > len(num) // 2:
                    break
                second = int(num[i : j])
                # print('second', second)
                third = first + second
                # print('third', third)
                start = j
                # print('first', first, 'second', second, 'third', third)
                # print('rest', num[start:])
                while num[start:].startswith('%d' % third):
                    start += len('%d' % third)
                    if start == len(num):
                        return True
                    # Do NOT modify first here!!!
                    tmp = second
                    second = third
                    third = tmp + second
                    print(third)
        return False

        