class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)/2):
            x = nums[i]
            y = nums[i + (len(nums)/2)]
            ans.extend([x,y])
        return ans
