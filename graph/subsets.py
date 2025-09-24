class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []

        def dfs(cur_index):
            result.append(subset[:])

            for i in range(cur_index, len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()

        dfs(0)

        return result
