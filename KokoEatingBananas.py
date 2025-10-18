class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, m = 1, max(piles), 0
        tempH = -1
        while l <= r:
            if tempH >= 0:
                r = m - 1
            else:
                l = m + 1
            tempH = h
            m = l + (r - l) // 2
            if m == 0:
                return 1
            for i in piles:
                if i % m != 0:
                    tempH -= (i // m) + 1
                else:
                    tempH -= i / m
        return m+1
