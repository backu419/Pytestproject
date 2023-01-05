import unittest
def mul(a,b):
    return a*b


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r=mul(5,2)
        self.assertEqual(r, 10)  # add assertion here


if __name__ == '__main__':
    unittest.main()
