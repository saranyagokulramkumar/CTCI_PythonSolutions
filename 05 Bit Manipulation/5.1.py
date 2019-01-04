# insert bits from M into N at positions j through i in N

import unittest
def updatebits(n,m,i,j):
    left = (1 << j+1)
    right = (1 << i)
    mask = ~(left - right)
    n = n & mask
    m = m << i
    return (n | m)
    
class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(updatebits(0b10000000000,0b10011,2,6),0b10001001100)
    
if __name__ == '__main__':
    unittest.main()
