# Uses Python3

def gcd(x, y):
         z = x % y
         if z == 0:
             return y
         else:
             return gcd(y, z)