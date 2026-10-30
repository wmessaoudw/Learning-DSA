from collections import defaultdict
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: #time o(n*m) #space o(n)

        count = [0] * 26
        anagram_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagram_map[key].append(s)
        return list(anagram_map.values())


class Solution2: #time o(m*nlogn) space o(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_value = {}
        output = []

        for i in range(len(strs)):
            str1 = ''.join(sorted(strs[i]))
            if str1 in sorted_value:
                sorted_value[str1].append(strs[i])
            else:
                sorted_value[str1] = [strs[i]]
        for i in sorted_value:
            output.append(sorted_value[i])
        return output
