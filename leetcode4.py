class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        L_1 = len(nums1)
        L_2 = len(nums2)
        lo = (L_1 + L_2) % 2
        k0 =int((L_1 + L_2) / 2)
        lo_1 = 0
        lo_2 = 0
        r_out = -1
        k = k0
        if lo == 0:
           k = k - 1
        while(1):
            if lo_1 >= L_1:
                if lo == 0:
                    r_out = (nums2[lo_2+k] + nums2[lo_2+k+1]) / 2
                else:
                    r_out = nums2[lo_2+k]
                break
            if lo_2 >= L_2:        
                if lo == 0:
                    r_out = (nums1[lo_1+k] + nums1[lo_1+k+1]) / 2
                else:
                    r_out = nums1[lo_1+k]
                break
            if k == 0:
                if lo == 0:
                    s_list = [nums1[lo_1],nums2[lo_2]]
                    if lo_1 + 1 < L_1:
                        s_list.append(nums1[lo_1+1])
                    if lo_2 + 1 < L_2:
                        s_list.append(nums2[lo_2+1])
                    s_list.sort()
                    r_out = float(s_list[0] + s_list[1]) / 2
                else:
                    r_out = min(nums1[lo_1],nums2[lo_2])
                break
            gap_1 = 0
            gap_2 = 0
            gap = int(k / 2)
            if lo_1 + gap < L_1:
                q1 = nums1[lo_1+gap]
            else:
                q1 = nums1[-1]
                gap_1 = L_1 - lo_1
            if lo_2 + k - gap - 1 < L_2:
                q2 = nums2[lo_2+k-gap-1]
            else:
                q2 = nums2[-1]
                gap_2 = L_2 - lo_2

            if q1 < q2:
                if gap_1 == 0:
                    lo_1 = lo_1 + gap + 1
                    k = k - gap - 1
                else:
                    lo_1 = lo_1 + gap_1
                    k = k - gap_1
            else:
                if gap_2 == 0:
                    lo_2 = lo_2 + k - gap
                    k = k - (k - gap)
                else:
                    lo_2 = lo_2 + gap_2
                    k = k - gap_2
        return r_out

cls = Solution()
print(cls.findMedianSortedArrays([1],[2,3,4,5]))
