class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        t=sum(max(accounts,key=sum))
        return t
        