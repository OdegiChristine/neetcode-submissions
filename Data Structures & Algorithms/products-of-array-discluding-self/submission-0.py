class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0] * len(nums)
        output = []

        # Find prefixes
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1] * nums[i])

        # Find suffixes
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i+1] * nums[i]

        for i in range(len(nums)):
            if (i - 1) < 0:
                pref = 1
            else:
                pref = prefix[i-1]

            if (i + 1) > len(nums) - 1:
                suf = 1
            else:
                suf = suffix[i+1]

            output.append(pref * suf)

        return output
        