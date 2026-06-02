# Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums, k):
        curr = sum(nums[:k])
        ans = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans / k