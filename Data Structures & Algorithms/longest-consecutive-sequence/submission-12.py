class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited = set()

        res = 0
        for n in nums_set:
            if n in visited:
                continue
            
            cur_len = 1
            pre_num, next_num = n - 1, n + 1
            while pre_num in nums_set:
                cur_len += 1
                visited.add(pre_num)
                pre_num -= 1
            
            while next_num in nums_set:
                cur_len += 1
                visited.add(next_num)
                next_num += 1 

            res = max(res, cur_len)

        return res