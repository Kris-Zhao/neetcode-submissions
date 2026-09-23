class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        left = 0
        maxf = 0
        res = 0

        for right in range(len(s)):
            if s[right] not in char_freq:
                char_freq[s[right]] = 0
            char_freq[s[right]] += 1

            maxf = max(maxf, char_freq[s[right]])

            # The window is valid as long as: window size – count of the most frequent character ≤ k
            while right - left + 1 - maxf > k:
                char_freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res