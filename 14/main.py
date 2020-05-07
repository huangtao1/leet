from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        if len(strs) == 0: return ""
        l = list(strs[0])
        s = ""
        for index, i in enumerate(l):
            flag = False
            for j in strs:
                if index > len(j) - 1:
                    return s
                if j[index] == i:
                    flag = True
                else:
                    return s
            if flag:
                s += i
        return s

    @staticmethod
    def zip_set(strs):
        s = ""
        tmp_lists = zip(*strs)
        for tmp_list in tmp_lists:
            if len(set(tmp_list)) == 1:
                s += tmp_list[0]
            else:
                break
        return s

    @staticmethod
    def horiz(strs):
        if len(strs) == 0: return ""
        # 水平匹配
        reg = strs[0]
        for i in strs[1:]:
            while i.find(reg) != 0:
                reg = reg[:-1]
                if reg == "":
                    return ""
        return reg


if __name__ == '__main__':
    print(Solution.horiz([]))
