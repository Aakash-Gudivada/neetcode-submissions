class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s1=s.sort()
        # t1=t.sort()
        # if s1==t1:
        #     return True 
        # return False 
        if len(s)!=len(t):
            return False 
        return sorted(s)==sorted(t)
        