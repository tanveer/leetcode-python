import unittest


class Solution:

    def backspace_compare(self, s1, s2):
        return self.is_same_string(s1) == self.is_same_string(s2)

    def is_same_string(self, s):

        output = []
        for char in s:
            if char == '#':
                if output:
                    output.pop()
            else:
                output.append(char)
        return str(output)


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test_backspace_compare(self):
        self.assertTrue(self.s.backspace_compare('ab#c', 'ad#c'))
        self.assertFalse(self.s.backspace_compare('a#c', 'b'))


if __name__ == "__main__":
    unittest.main()
