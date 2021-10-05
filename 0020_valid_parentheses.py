import unittest


class Solution:
    def validParentheses(self, str):
        map = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in str:
            if c in map:
                top = stack.pop() if stack else '#'
                if map[c] != top:
                    return False
                else:
                    stack.append(c)

            return not stack


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test_validParentheses(self):
        self.assertFalse(not self.s.validParentheses('(]'))
        self.assertEqual(self.s.validParentheses('{([({})])}'), True)
        self.assertEqual(self.s.validParentheses('()'), True)


if __name__ == '__main__':
    unittest.main()
