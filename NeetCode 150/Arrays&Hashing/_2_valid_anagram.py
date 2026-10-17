class Solution1: # o(nlogn) time o(n) space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()

        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return False
        return True


class Solution2:#o(n) time o(n) space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        test_dic = dict()
        test_dic2 = dict()

        for i in range(len(s)):
            test_dic[s[i]] = test_dic.get(s[i], 0) + 1
            test_dic2[t[i]] = test_dic2.get(t[i], 0) + 1

        if test_dic != test_dic2:
            return False
        for i in test_dic:
            if test_dic[i] != test_dic2[i]:
                return False
        return True


class Solution3: #o(n) time o(n) space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        test_dic = dict()

        for i in range(len(s)):
            test_dic[s[i]] = test_dic.get(s[i], 0) + 1
            test_dic[t[i]] = test_dic.get(t[i], 0) - 1

        for i in test_dic.values():
            if i != 0:
                return False
        return True


