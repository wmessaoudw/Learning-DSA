from typing import List


class mySolution:
    # Time Complexity: O(N + K * U), where N is the length of nums and U is the number of unique elements.
    # Space Complexity: O(N + K) for the frequency dictionary, set, and output array.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = ['a'] * k
        counter = {}

        insert = 0
        already_seen = set()
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        for index in range(k):
            temp = 0
            for i in counter:
                if counter[i] > temp and i not in output:
                    insert = i
                    temp = counter[i]

            output[index] = insert
        return output
import heapq
from collections import Counter
from typing import List


class Solution1:
    # Time Complexity: O(N log K), where N is the length of nums and K is the number of top elements.
    # Space Complexity: O(N) for the frequency dictionary and min-heap.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]
from typing import List


class Solution2:
    # Time Complexity: O(N), where N is the length of nums.
    # Space Complexity: O(N) for the frequency dictionary, bucket array, and output list.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        output = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for num, freq in count.items():
            frequency[freq].append(num)
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                output.append(n)
                if len(output) == k:
                    return output

        return output