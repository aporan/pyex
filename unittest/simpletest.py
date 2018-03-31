import unittest

## Actual Functions

def is_even(n):
    res = n / 2
    return res

## Testing Part

class IsEvenTest(unittest.TestCase):

    def test_number_is_even(self):
        number = 4
        res = is_even(number)
        self.assertTrue(res)

if __name__=="__main__":
    unittest.main()
