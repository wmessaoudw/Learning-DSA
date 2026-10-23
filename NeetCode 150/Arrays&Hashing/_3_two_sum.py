class Solution1:# time o(n^2)  space o(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target and i!=j:
                    pairs.append(i)
                    pairs.append(j)
                    return pairs


class Solution2: # time o(n)  space o(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        index_dict = dict()
        for i in range(len(nums)):
            diffrence = target - nums[i]

            if diffrence in index_dict:
                return [index_dict[diffrence], i]
            else:
                index_dict[nums[i]] = i







