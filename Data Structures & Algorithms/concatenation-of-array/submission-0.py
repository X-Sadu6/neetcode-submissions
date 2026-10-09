class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        Nums2 = list(nums) + []
        for num in nums:
            Nums2.append(num)
        return Nums2
        
        
        