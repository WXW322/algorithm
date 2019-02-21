#include<iostream>
#include<vector>
#include<cmath>
# define max_int 0x3FFF
using namespace std;

class Solution {
    public:
            int minPathSum(vector<vector<int> >& grid) {
                        int t_line = (int)grid.size();
                        int t_col = (int)grid[0].size();
                        int minimum[t_line + 1][t_col + 1];
                        minimum[0][0] = grid[0][0];
                        for(int i = 0;i < t_line;i++)
                        {
                            for(int j = 0;j < t_col;j++)
                            {
                                int t_left = max_int;
                                int t_up = max_int;
                                if(i - 1 >= 0)
                                {
                                    t_up = minimum[i-1][j] + grid[i][j];
                                }
                                if(j - 1 >= 0)
                                {
                                    t_left = minimum[i][j-1] + grid[i][j];
                                }
                                int t_min = min(t_up,t_left);
                                if(t_min < max_int)
                                {
                                    minimum[i][j] = t_min;
                                }
                                else
                                {
                                    minimum[i][j] = grid[i][j];
                                }


                            }
                        }
                        return minimum[t_line - 1][t_col - 1];

                    }
};
int main()
{
    vector<vector<int> > g_v;
    vector<int> g_s,g_m;
    g_s.push_back(1);
    g_s.push_back(2);
    g_m.push_back(3);
    g_m.push_back(1);
    g_v.push_back(g_s);
    g_v.push_back(g_m);
    Solution A = Solution();
    cout<<A.minPathSum(g_v)<<endl;
    return 1;
}
