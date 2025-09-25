# this solution was timed out
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        path = ["JFK"]
        num_tickets = len(tickets)
        
        def dfs():
            if len(path) == num_tickets + 1:
                return True
            
            for i in range(len(tickets)):
                from_airport, to_airport = tickets[i]
                
                if path[-1] == from_airport:
                    used_ticket = tickets.pop(i)
                    path.append(to_airport)
                    
                    if dfs():
                        return True
                    
                    path.pop()
                    tickets.insert(i, used_ticket)
            
            return False

        dfs()
        return path
