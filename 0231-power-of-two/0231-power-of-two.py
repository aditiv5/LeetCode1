class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n)[2:].replace('0', '') == '1'