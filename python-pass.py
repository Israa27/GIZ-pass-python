class Solution:
    @staticmethod
    def longest_palindromic(s: str) -> str:
        def expandAroundCenter(left,right):
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
            return s[left+1:right]
        logestSub=""
        for i in range(len(s)):
            test=expandAroundCenter(i,i)
            if len(test)>len(logestSub):
               logestSub=test
            test=expandAroundCenter(i,i+1)
            if len(test)>len(logestSub):
               logestSub=test
        return logestSub
