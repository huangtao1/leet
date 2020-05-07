class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        if x > pow(2, 31) - 1 or x < pow(-2, 31):
            return 0
        if x >= 0:
            x = int(str(x)[::-1])
        if x < 0:
            x = int("-" + str(x)[:0:-1])
        if x > pow(2, 31) - 1 or x < pow(-2, 31):
            return 0
        return x


if __name__ == '__main__':
    print(Solution.reverse(243))
    print(Solution.reverse(-243))
