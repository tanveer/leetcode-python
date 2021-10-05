import unittest

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}


class Solution:
    def twoSum1(self, nums, target):
        """
            Time: O(n)
            Space: O(n)
        """
        map = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in map:
                return [map[compliment], i]
            else:
                map[nums[i]] = i
        return [-1, -1]

    def twoSum2(self, nums, target):
        """
            Time: O(n^2)
            Space: O(1) 
        """
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]


class Test(unittest.TestCase):

    def setUp(self):
        self.s1 = Solution()
        self.s2 = Solution()

    def tearDown(self):
        pass

    def test_twoSum(self):
        self.assertEqual(self.s1.twoSum1([2, 7, 11, 15, 9], 9), [0, 1])
        self.assertEqual(self.s1.twoSum1([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.s2.twoSum2([3, 3], 6), [0, 1])
        self.assertEqual(self.s2.twoSum2([3, 3, 4, 1, 0, 6], 100), [-1, -1])


if __name__ == '__main__':
    unittest.main()
