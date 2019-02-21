import sys
class Solution:
    def transp(self,p):
        length = len(p)
        if length == 0:
            return p
            
        p_new = ''
        for i in range(len(p)):
            if p_new == '':
                p_new = p[i]
            elif p_new[-1] == '*':
                if p[i] == '*':
                    continue
                else:
                    p_new = p_new + p[i]
            else:
                p_new = p_new + p[i]
        lo = 0
        for i in range(len(p_new)):
            if p_new[i] != '*':
                break
        p_new = p_new[i:]
        return p_new

    def comp(self,a,b):
        if b == ".":
            return True
        elif a == b:
            return True
        else:
            return False

    def isMatch(self, s, p):
         """
         :type s: str
         :type p: str
         :rtype: bool
         """
         p = self.transp(p)
         len_one = len(s)
         len_two = len(p)
         if len_one == 0:
            if len_two == 0:
                return True
            if len_two != 0 and p[0] == "*":
                return True
            else:
                return False
         elif len_two == 0 and len_one != 0:
            return False
            
            
         states = [[False for _ in range(len_two + 1)] for _ in range(len_one + 1)]
         states[0][0] = self.comp(s[0],p[0])
         for i in range(1,len_one):
             states[i][0] = False
         for j in range(1,len_two):
             for i in range(len_one):
                 now_v = p[j]
                 pre_v = p[j-1]
                 if i == 0:
                    if now_v == '*':
                        states[i][j] = states[i][j-1]
                    else:
                        states[i][j] = False
                    continue
                 if now_v == '.':
                    states[i][j] = states[i-1][j-1]
                 elif now_v == '*':
                    if pre_v == '.':
                        t_lo = 0
                        t_p = i
                        while(t_p >= 0):
                            if states[t_p][j-1]:
                                t_lo = 1
                                break
                            t_p = t_p - 1
                        if t_lo == 1:
                            states[i][j] = True
                    else:
                        t_lo = 0
                        t_p = i
                        if states[i][j-1]:
                            states[i][j] = True
                            continue
                        while(t_p > 0 and pre_v == s[t_p]):
                            if states[t_p-1][j-1]:
                                t_lo = 1
                                break
                            t_p = t_p - 1
                        if t_lo == 1:
                            states[i][j] = True

                 else:
                    if self.comp(s[i],p[j]):
                        states[i][j] = states[i-1][j-1]
                    else:
                        states[i][j] = False
         for state in states:
             print(state)
         return states[len_one-1][len_two-1]
ss = Solution()
print(ss.isMatch("aab","c*a*b"))

