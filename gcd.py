# Uses Python3
def gcd(x, y):
         z = x % y
         if z != 0:
             return gcd(y, z)
         return y