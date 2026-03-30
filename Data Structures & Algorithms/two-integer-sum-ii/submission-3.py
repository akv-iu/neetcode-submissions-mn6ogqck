class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        b = 0
        e = len(numbers) - 1

        while b<e:
            if numbers[b]+numbers[e] > target:
                e-=1
            elif numbers[b]+numbers[e] < target:
                b+=1
            else:
                return([b+1,e+1])
        
        