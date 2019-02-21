class Solution:
    def isMatch(self, s, p):
         """
         :type s: str
         :type p: str
         :rtype: bool
         """
         len_s = len(s)
         len_p = len(p)
         states = [[False for _ in range(len_p+2)] for _ in range(len_s+2)]
         states[0][0] = True
         if len_p == 0:
            return states[len_s][len_p]
         states[1][1] = True if p[0] == '.' or p[0] == s[0] else False 
         for i in range(2,len_p+1):
             states[0][i] = states[0][i-2] if p[i-1] == '*' else False
         print(states)
         for i in range(1,len_s+1):
             for j in range(2,len_p+1):
                 if p[j-1] != '*':
                    print(i,j)
                    print(s[i-1],p[j-1])
                    states[i][j] = states[i-1][j-1] if (p[j-1] == '.' or s[i-1] == p[j-1]) else False
                 else:
                    if states[i][j-2]:
                        states[i][j] = states[i][j-2]
                        continue
                    else:
                        states[i][j] = states[i-1][j] if (s[i-1] == p[j-2] or p[j-2] == '.') else False
         for state in states:
             print(state)
         return states[len_s][len_p]
ss = Solution()
print(ss.isMatch("aab","c*a*b"))
