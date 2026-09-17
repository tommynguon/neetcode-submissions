class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1 #we haven't seen this num yet so we start the count at one

        pairs = []
        for num in count:
            pairs.append((count[num],num))

        pairs.sort(reverse = True)

        results = []
        for i in range(k):
            results.append(pairs[i][1])
        return results

            