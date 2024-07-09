import random
def fuct(l,mymax = 0):
    if not l :
        return mymax
    return fuct(l[1:],max(mymax,l[0]))


#num = [random.randint(0, 99) for _ in range(5)]
#print(num)
#print(fuct(num))

def posNum(l, acc=0):
    if not l:
        return acc
    elif l[0]>0 or l[0] == 0:
        return posNum(l[1:],acc+l[0])
    elif l[0]<0:
        return posNum(l[1:],acc)

#num = [random.randint(-999, 999) for _ in range(50)]
#print(num)
#print(posNum(num))

def myReverse(l, acc=""):
    if not l:
        return acc
    return myReverse(l[:-1],acc+l[-1])

#myL = "hello u r"
#print(myReverse(myL))

def minNum(l, acc=0):
    if not l:
        return acc
    return minNum([l[0] if l[0] < acc else acc])

num = [random.randint(-999, 999) for _ in range(50)]
print(num)
print(minNum(num))