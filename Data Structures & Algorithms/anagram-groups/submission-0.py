class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # mapping character count to list

        for s in strs:
            count = [0] * 26 # a -> z
        
            # this uses ascii values to assign indexes to the right letter
            #so if c = "a" -> count[0] += 1
            for c in s:
                count[ord(c) - ord("a")] += 1 

            res[tuple(count)].append(s) #must be a tuple as must be immutabel 

        return list(res.values())





        