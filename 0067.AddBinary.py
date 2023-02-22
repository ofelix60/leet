class Solution(object):
    def addBinary(self, a, b):
        aBin = int(a, 2)
        bBin = int(b, 2)
        sum = aBin + bBin
        return bin(sum).replace("0b", "")


solution = Solution()

print(
    solution.addBinary(
        "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
        "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011",
    )
)
