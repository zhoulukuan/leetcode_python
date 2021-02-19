class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend * divisor > 0: symbol = 1
        else: symbol = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        # 特殊情况处理
        if dividend == 0 or dividend < divisor: return 0
        # 越界问题,当除数为-1,被除数为-2**31的时候,商为2**31-1需要进行截断 
        if divisor == 1: return 2**31-1 if dividend == 2**31 and symbol == 1 else dividend * symbol

        # 获取范围,lo为下界,hi为上界(包含)
        i = 0
        while (dividend >> i) >= divisor: i += 1
        lo, hi = 2**(i - 1), 2**i

        while lo < hi:
            medium = int((lo + hi) >> 1)
            num = medium * divisor
            if num == dividend: return symbol * medium
            elif num > dividend: hi = medium
            # 此处可能会出现lo+1后导致lo*除数刚好大于被除数的情况,因此最后统一处理
            else: lo = medium + 1

        if lo * divisor == dividend: return symbol * lo
        else: return symbol * (lo - 1)
