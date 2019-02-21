
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        t_len = len(s)
        t_x = t_len
        t_y = numRows
        t_r = [[-1 for col in range(t_y)] for row in range(t_x)]
        i = 0
        t_lo = 0
        line = 0
        col = 0
        while(i < t_len):
            if(t_lo == 0):
                t_r[line][col] = s[i]
                i = i + 1
                col = col + 1
                if(col >= numRows):
                    t_lo = 1
                    col = col - 1
            else:
                col = col -1
                line = line + 1
                if(col >= 0):
                    t_r[line][col] = s[i]
                    i = i + 1
                if(col == 0):
                    col = 1
                    t_lo = 0
                elif(col < 0):
                    col = 0
                    t_lo = 0
        t_s = []
        for j in range(numRows):
            for i in range(line):
                if(t_r[i][j] != -1):
                    t_s.append(t_r[i][j])
        t_ss = ''.join(t_s)
        return t_ss


ss = Solution()
ss.convert(s = "heltfchqssrwqgwanggkjlsownsdpoowubszfzratjwlpuldarnmehcbvuemiulcxdedcxfygbjyyxbyqqmvxoyukchszuxwxdbbagzjklhiikiyavvzltwwyfqxzpvwszxvfzerknbuxkszhoaujwqhbjecycyrbyoizucjhddgpxfynftxelehulktnkkqkaajucsdgxjvvoukvphzamjvxtomfacqaezwhuzntkkqagbvxkxywgtvbjjijnylsajzwioruaiujlrgvoguwzrzkbivogggiphgzvytygnhtfnovwkuvctidbdrkkaubhbddzwbhmkatzqqvbktdgbgjezvqzqshtxmutpbhzdcyvvwwhpbnqjxujunkmhtfehzzwchxhlydiubqjddbmcxxzkilrdrvlsvjvehcrfhabjqkmvnaykyxviimnbkyufirlpvcwdcxmsjaowaogandkxsybcwvjgouxjytobscvdclbfzkfonqmfqpjmksvaoslnoaqgelmhxnmyxtnllbsbqcocwjendparrsywdkfazrbxmoiyrczjgplfypseguvymvuphzshsteejoccsclzrwesnyytsttgppvwqpfikjpvztxsxirrgxlvvjpnckttaqqqivbshsogllylwrccopylypaabvwbomuwjxqspezcszpqtrsjgsvgjxhltdohrifchvvyawbuxqkskecszzzkyixrnmagwfiebfcdbfxbyjtipxcoybzxjyowkrcjwnpxstawbzxzisjysloqnpnyoevavzjrmarhutdvtcwdwfdoqsffhuexazyvajpnkiugbzdwdzazedowxvchrgeshephogwaosiqtlmwmowssmopjswayduhhkrxqnzhijxbulyiawauirjtjitk"
, numRows = 742)
