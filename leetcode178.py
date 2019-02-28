class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        t_temp = {}
        if len(buildings) == 0:
            return []
        start = buildings[0][0]
        end = buildings[-1][1]
        i = start
        while(i <= end):
            t_temp[i] = 0
            i = i + 1
        for build in buildings:
            p_start = build[0]
            p_end = build[1]
            p_h = build[2]
            t_i = p_start
            while(t_i <= p_end):
                if t_temp[t_i] < p_h:
                    t_temp[t_i] = p_h
                t_i = t_i + 1
        
        t_list = [[key, t_temp[key]] for key in t_temp]
        t_list.sort(key = lambda x:x[0])
        t_f = []
        h_line = -1
        i = 0
        count = end - start
        while(i <= count):
            if(t_list[i][1] != h_line):
                if t_list[i][0] == start:
                    t_f.append([t_list[i][0], t_list[i][1]])
                    h_line = t_list[i][1]
                else:
                    if(t_list[i][1] > t_list[i-1][1]):
                        t _f.append([t_list[i][0], t_list[i][1]])
                        h_line = t_list[i][1]
                    else:
                        t_f.append([t_list[i-1][0], t_list[i][1]])
                        h_line = t_list[i][1]
            i = i + 1
        t_f.append([end, 0])
        return t_f
        
