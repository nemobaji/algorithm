class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []

        def dfs(start_num):
            if len(combination) == k:
                result.append(combination[:])
                return
              
            for i in range(start_num, n + 1):
                combination.append(i)
                dfs(i + 1)
                combination.pop()

        dfs(1)
        return result
