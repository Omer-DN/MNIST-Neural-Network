#
# myboolfuncs module
import math
#
def isNumber(valStr):
   if valStr.count('.') > 1:
     return False
   L = [c for c in valStr  if (c.isdigit() or c == '.')]
   return len(L) == len(valStr)
#
def getNumber(prompt):
   while True:
     val = input(prompt)
     if not isNumber(val):
       print ("it must be a number!")
     else:
       return eval(val)


def is_valid_triangle(a, b, c):
    # בודקים את אי שוויון המשולש
    if a + b > c and a + c > b and b + c > a:
        print("lengths sides triangle correct\n")
        s = (a + b + c) / 2
        # מחשבים את השטח באמצעות נוסחת הרון
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        print("lengths sides triangle incorrect")
        return False