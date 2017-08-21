#題目 nums為一個數字list target為一數字 求nums當中兩個數字和為target之該兩個數字的index
class Solution(object):
    def twoSum(self, nums, target):
        ＃例外處理
        if len(nums) <=1:
            return False
        num_dict={}
        for i in range(len(nums)):
            ＃判斷當數字存在於num_dict當中時num_dict[nums[i]]
            if nums[i] in num_dict:
                return [num_dict[nums[i]],i]
            else:
                print ("target: %d - nums[i]: %d = %d"%(target,nums[i],i))
                ＃key為target與該數字的差 value為該數字在nums中的index
                num_dict[target- nums[i]]=i
a = Solution().twoSum([1,2,3,4,5],7)
print (a)