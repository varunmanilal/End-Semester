from Functions import *
import math
def func(x):
    #The function
    p = (x-5)*math.exp(x)+5
    return p
#u is the root
(u,v)=newtonraph(17,func,0.0001)
print("The root is obtained as ",u)
#u = hc/(\lambda)*kT
#To find value of b using the formula
b = 6.626*pow(10,-34)*3*pow(10,8)/(u*1.381*pow(10,-23))
#printing value of b
print("b = \lambda T is calculated as ",round(b,5))

# The root is obtained as  4.965114231973995
# b = \lambda T is calculated as  0.0028990103306041647(if not rounded)
#b = \lambda T is calculated as  0.0029