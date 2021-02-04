from Functions import *
#First function
def funcf(z):
    p=z
    return p
#Second function
def funcg(x,y,z):
    p=-9.8
    return p
#y(0)=2
#y(5)=45
yn=45
#Taking 2 input estimates
def estimate():
    for i in range(20):
        est1 = input("Estimate 1st value for slope ")
        zh = float(est1)
        est2 = input("Estimate 2nd value for slope ")
        zt = float(est2)
        (X1, Y1) = RK4(0, 2, zh, 0.01, 5, funcf, funcg)
        (X2, Y2) = RK4(0, 1, zt, 0.01, 5, funcf, funcg)
        #If for both points yn is on one side then estimate again
        if (Y2[99]>yn and Y1[99]>yn) or (Y2[99]<yn and Y1[99]<yn):
            print("Give another set")
            continue
        else:
            return zh, zt
(zh,zt) = estimate()
#Using shooting method
a,b,c,d=shootingmethod(funcf,funcg,45,zh,zt)
print("The launch velocity is: ",d)

# Estimate 1st value for slope 40
# Estimate 2nd value for slope 50
# The launch velocity is:  48.89999999999995