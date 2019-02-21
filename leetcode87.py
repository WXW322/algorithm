import time
class Solution(object):
    def isScramole(self,s1,s2):
        """
        :type s1:str
        :type s2:str
        :rtype bool
        """
        return self.get_stwo(s1,s2) 
                
    def merge_r(self,r_one,r_two):
        """
        function:merge results of two nodes
        :type r_one:list for left node
        :type r_two:list for right node
        :rtype merge results
        """
        t_f = set()
        for one in r_one:
            for two in r_two:
                t_f.add(one + two)
        for two in r_two:
            for one in r_one:
                t_f.add(two + one)
        return t_f

    def get_substr(self,sub_str):
        """
        function:get all posible scramble string of sub_str
        :rtype sub_str:str 
        :rtype all posible scramble strings
        """
        if sub_str in self.words:
            return self.words[sub_str]
        t_len = len(sub_str)
        i = 1
        if t_len == 0:
            return [""]
        if t_len == 1:
            return [sub_str]
        t_finals = {}
        while(i < t_len):
            if sub_str[0:i] in self.words:
                left_node = self.words[sub_str[0:i]]
            else:
                left_node = self.get_substr(sub_str[0:i])
                self.words[sub_str[0:i]] = left_node
            if sub_str[i:t_len] in self.words:
                right_node = self.words[sub_str[i:t_len]]
            else:
                right_node = self.get_substr(sub_str[i:t_len])
                self.words[sub_str[i:t_len]] = right_node
            t_rA = self.merge_r(left_node,right_node)
            for idom in t_rA:
                t_finals[idom] = 1
            i = i + 1
        self.words[sub_str] = t_finals
        return t_finals
    
    def get_stwo(self,s_one,s_two):
        if(len(s_one) != len(s_two)):
            return False
        t_len = len(s_one)
        t_dic = [[[0 for i in range(t_len + 1)] for i in range(t_len + 1)] for i in range(t_len + 1)]
        for i in range(t_len):
            for j in range(t_len):
                if s_one[i] == s_two[j]:
                    t_dic[i][j][1] = True
        l = 2
        while(l <= t_len):
            for i in range(t_len - l + 1):
                for j in range(t_len -l + 1):
                    for ll in range(l):
                        t_lo = ((t_dic[i][j][ll]) & (t_dic[i+ll][j+ll][l-ll])) | ((t_dic[i][j+l-ll][ll]) & (t_dic[i+ll][j][l-ll]))
                        if(t_lo):
                            t_dic[i][j][l] = True
                            break
            l = l + 1
        print(t_dic)
        return t_dic[0][0][t_len]

start = time.time()
A = Solution()
print(A.isScramole("great","rgeat",))
end = time.time()
print(end - start)
