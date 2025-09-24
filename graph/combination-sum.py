class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def dfs(current_sum, start_index):
            if current_sum == target:
                result.append(combination[:])
                return
            
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                combination.append(candidates[i])
                dfs(current_sum + candidates[i], i) 
                combination.pop()

        dfs(0, 0)
        return result
