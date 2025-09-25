class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for start, destination in sorted(tickets):
            graph[start].append(destination)
        
        result = []

        def dfs(start):
            while graph[start]:
                next_destination = graph[start].pop(0)
                dfs(next_destination)

            result.append(start)

        dfs("JFK") 
        
        return result[::-1]
