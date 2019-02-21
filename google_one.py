import sys


filein = open('a.in','r')
fileout = open('data.out','w+')
ss = sys.stdin
sys.stdin = filein
so = sys.stdout
sys.stdout = fileout
T = int(input())

i = 1
while(i <= T):
    N,M,P = map(int,input().split())
    j = 1
    t_dic = {}
    t_f = []
    t_num = []
    while(j <= N):
        t_S = str(input())
        p = 0
        while(p < P):
            t_idom = t_S[p]
            if(p not in t_dic):
                t_dic[p] = {}
            if(t_idom not in t_dic[p]):
                t_dic[p][t_idom] = 1
            else:
                t_dic[p][t_idom] = t_dic[p][t_idom] + 1
            p = p + 1
        j = j + 1
    t_M = str(input())
    t_MM = list(t_M)
    t_min = 1000
    p = 0
    while(p < P):
        t_key = '0'
        t_max = 0
        if '0' in t_dic[p]:
            t_z = t_dic[p]['0']
        else:
            t_z = 0
        if '1' in t_dic[p]:
            t_one = t_dic[p]['1']
        else:
            t_one = 0
        if(t_z > t_one):
            t_key = '0'
            t_max = t_dic[p]['0']
        else:
            t_key = '1'
            t_max = t_dic[p]['1']
        t_f.append((t_key,t_max))
        p = p + 1
    t_lo = 0
    p = 0
    t_fsum = 0
    t_minlo = 0
    while(p < P):
        if(t_f[p][0] != t_MM[p]):
            t_lo = 1
        if(t_f[p][1] < t_min):
            t_min = t_f[p][1]
            t_minlo = p
        t_fsum = t_fsum + (M - t_f[p][1])
        p = p + 1
    if (t_lo == 0):
        t_fsum = t_fsum - (t_f[t_minlo][1] - (M - t_f[t_minlo][1]))
    print("Case #%d: %d"%(i,t_fsum))
    i = i + 1


