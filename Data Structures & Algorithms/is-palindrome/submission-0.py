class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        result = ""
        for c in s:
            if c.isalnum():
                result += c.lower()
        print(result)
        end = len(result) - 1

        while start<end:
            if result[start] == result[end]:
                start += 1
                end -= 1
                print(start)
                continue
            else:
                return False
        
        return True

        
        