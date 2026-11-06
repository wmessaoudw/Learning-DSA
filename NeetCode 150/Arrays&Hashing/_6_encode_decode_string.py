class Solution1: #time o(n^2) space o(n)

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for i in range(len(strs)):

            for j in range(len(strs[i])):
                encoded_string = encoded_string + strs[i][j]
            encoded_string = encoded_string + '—'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        index = 0
        temp = ''
        for i in range(len(s)):

            if s[i] != '—':
                temp = temp + s[i]
            else:
                decoded_string.append(temp)
                temp = ''
        return decoded_string


class Solution2: #time o(n) space o(n)

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:length + j + 1])
            i = j + 1 + length
        return res