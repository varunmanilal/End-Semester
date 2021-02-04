from Functions import *
import math
#reading data file downloaded from classroom and renamed as q3.dat
f1 = open('q3.dat','r')
a = f1.read()
a1 = [item.split('\t') for item in a.split('\n')]
X=[]
Y=[]
#len(a1)-2 since last two rows are empty and not necessary
for i in range(2,len(a1)-2):
    X.append(float(a1[i][0]))
    Y.append(float(a1[i][-1]))
#X is time and Y is angular velocity
print("List for time",X)
print("List for angular velocity",Y)
#Least square fit for 1st Equation
a,b,c,d,e,f=LeastSquare(X,Y)
print("Equation 1")
print("The intercept(w0) is ",a," and the slope(wc) is ",b)
print("Pearson's r is calculated as: ",f)
#2nd equation is log(w)=log(w0)-wc*t
for i in range(len(Y)):
    Y[i]=math.log(Y[i],math.e)
#Least Square Fit for 2nd equation
a,b,c,d,e,f=LeastSquare(X,Y)
print("Equation 2")
print("The intercept(log(w0)) is ",a," and the slope(-wc) is ",b)
print("Pearson's r is calculated as: ",f)

# List for time [0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3]
# List for angular velocity [2.2, 1.96, 1.72, 1.53, 1.36, 1.22, 1.1, 1.0, 0.86, 0.75, 0.65, 0.6]
# Equation 1
# The intercept(w0) is  2.0291025641025655  and the slope(wc) is  -0.4747086247086251
# Pearson's r is calculated as:  0.97053188449053
# Equation 2
# The intercept(log(w0)) is  0.7902775293458726  and the slope(-wc) is  -0.3955961745485569
# Pearson's r is calculated as:  0.9982366554936281
