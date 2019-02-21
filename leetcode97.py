class Solution(object):
   def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            if(s2 == s3):
                return True
            else:
                return False
        if len(s2) == 0:
            if(s1 == s3):
                return True
            else:
                return False

        state = [[[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] for i in range(len(s3) + 1)]
        if s1[0] == s3[0]:
            state[1][1][0] = 1
        if s2[0] == s3[0]:
            state[1][0][1] = 1

        for L in range(2,len(s3) + 1):
            for L_one in range(0,min(len(s1) + 1,L + 1)):
                if L-L_one > len(s2):
                    continue
                s_one = 0
                s_two = 0
                if (L_one > 0 and state[L-1][L_one-1][L-L_one] and s3[L-1] == s1[L_one-1]):
                    s_one = 1
                if (L-L_one > 0 and state[L-1][L_one][L-L_one-1] and s3[L-1] == s2[L-L_one-1]):
                    s_two = 1
                state[L][L_one][L-L_one] = (s_one or s_two)
        if(state[L][len(s1)][len(s2)] == 1):
            return True
        else:
            return False

ss = Solution()
print(ss.isInterleave("aabcc","dbbca","aadbbbaccc"))


                        
        
         



