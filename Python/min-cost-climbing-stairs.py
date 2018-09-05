# Time:  O(n)
# Space: O(1)
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev, current = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev, current = current, min(prev, current) + cost[i]
        return min(prev, current)
        
    def minCostClimbingStairs1(self, cost):
        prev, current = 0, min(cost[0], cost[1])
        for i in range(2, len(cost)):
            prev, current = current, min(cost[i]+current, cost[i-1]+prev)
        return current