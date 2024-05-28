class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        if len(set(s))!=len(set(t)):
            return False
        for  i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
            else:
                if t[i]!=d[s[i]]:
                    return False
        return True