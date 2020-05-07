# 回文数
class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_number = 0
        while x > reverse_number:
            reverse_number = reverse_number * 10 + x % 10
            x //= 10
        return x == reverse_number or x == reverse_number // 10

    @staticmethod
    def is_palindrome(x: int) -> bool:
        # 字符串解决
        # return False if x<0 else str(x)[::-1] == str(x)
        if x < 0:
            return False
        else:
            return str(x)[::-1] == str(x)


if __name__ == '__main__':
    print(Solution.isPalindrome(1221))
