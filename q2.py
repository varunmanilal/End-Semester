from Functions import *
import math
#a as specified
a = math.sin(math.pi/8)
#the function is given as
def func(x):
    #The function is given as
    p = 4*pow(9.8,-0.5)*(1/math.sqrt(1-(pow(a,2)*pow(math.sin(x),2))))
    return p
#The integrated sum is
sum = simpson(0,math.pi/2,10,func)
print("The time period of oscillation is: ",sum)

#The time period of oscillation is:  2.087320017479592
