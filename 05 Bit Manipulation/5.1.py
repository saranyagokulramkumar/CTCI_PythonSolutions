# insert bits from M into N at positions j through i in N

import unittest
def updatebits(n,m,i,j):
    left = (1 << j+1) # create a left mask with 1 at j+1th position
    right = (1 << i) # create a right mask with 1 at ith position
    mask = ~(left - right) # subtract left from right to get 1's at positions j through i and negate it to get 0s
    n = n & mask # clear bits in n using the mask
    m = m << i # shift m i bits
    return (n | m) # sub'ing bits in n with corresponding ones in positions j through i in m
    
class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(updatebits(0b10000000000,0b10011,2,6),0b10001001100)
    
if __name__ == '__main__':
    unittest.main()
