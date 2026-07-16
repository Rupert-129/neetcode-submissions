class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_m = {} # empty hashmap

        for i, n in enumerate(nums): #enumerate assigns indicies to numbers
            diff = target - n #subtracts the number from the target to get a difference
            if diff in hash_m: #checks if we have seen the difference before
                return [hash_m[diff], i] # if so returns an array of the index where the difference appeared and the current number
            hash_m[n] = i #if the difference isnt present we need to add it to the hash map.
        return #if we werent guarenteed an answer this would return nothing 
        
        
            



        


    

