class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0 #low point at the first index
        high = len(nums) - 1 #high point on the last index
        
        while low <= high:
            mid = (high + low) // 2 # find midpoint // creates an integer
            
            if nums[mid] == target:
                return mid #if the middle is our answer
            elif target < nums[mid]:
                high = mid - 1 #cuts the sample in half to only leave the lower half
            else:
                low = mid + 1 #leaves upper half
        
        return -1 #if not on list -> minus 1


        