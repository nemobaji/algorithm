# --- this solution timed out                                                        
# class Solution:                                                                     
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:  
#         graph = collections.defaultdict(list)                                      
#         for a, b in prerequisites:
#             graph[a].append(b)
#
#         traced = set()
#
#         def dfs(i):
#             if i in traced:
#                 return False
#
#             traced.add(i)
#             for y in graph[i]:
#                 if not dfs(y):
#                     return False
#             traced.remove(i)
#
#             return True
#
#         for x in list(graph):
#             if not dfs(x):
#                 return False
#
#         return True

class Solution: # 가지치기를 통한 최적화
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
