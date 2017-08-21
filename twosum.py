class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <=1:
            return False
        num_dict={}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                return [num_dict[nums[i]],i]
            else:
                print ("target: %d - nums[i]: %d = %d"%(target,nums[i],i))
                num_dict[target- nums[i]]=i
a = Solution().twoSum([1,2,3,4,5],7)
print (a)