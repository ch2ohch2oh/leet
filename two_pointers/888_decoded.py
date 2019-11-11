class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # print('decodeAtIndex', S, K)
        start = 0
        total = 0
        partial = 0
        for i in range(len(S)):
            if S[i].isalpha():
                partial += 1
                if total + partial == K:
                    return S[i]
            elif S[i].isdigit():
                rep = int(S[i])
                if (total + partial) * rep < K:
                    total = (total  + partial) * rep
                    partial = 0
                    start = total
                else:
                    pos = (K) % (total + partial)
                    if pos == 0:
                        return self.decodeAtIndex(S[:i], total + partial)
                    else:
                        return self.decodeAtIndex(S[:i], pos)
            # print(i, 'partial', partial, 'total', total)