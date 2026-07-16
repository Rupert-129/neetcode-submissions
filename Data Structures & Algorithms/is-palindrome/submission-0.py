class Solution:
    def isPalindrome(self, s: str) -> bool:

        newstr = "" #create new string

        for i in s: #for an element of the string
            if i.isalnum(): #if alphanumeric
                newstr += i.lower() #add to this list and make it lowercase
        return newstr == newstr[::-1] #compare to reversed list (newstr[::-1] is the reversed list)