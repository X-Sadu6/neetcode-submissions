class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Seen = set(list(nums))
        if len(nums)==len(Seen):
            return False
        else:
            return True