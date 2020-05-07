class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        total = 0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sd = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        for k, v in sd.items():
            a = s.count(k)
            total += a * v
            s = s.replace(k, '')
            if len(s) == 0:
                return total
        for k, v in d.items():
            a = s.count(k)
            total += a * v
        return total


if __name__ == '__main__':
    print(Solution.romanToInt("MCMXCIV"))
