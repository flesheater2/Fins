import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

print("for flat fin type = '1' and cylindrical fin type = '2' ")

jk = int(input("type: "))
L = l_fin = float(input("length of the fin (L in meters): "))
if (jk == 2):
    d = float(input("dia of the fin (d in meters): "))
    r = float(d/2)
    A_val = float(3.14*r*r)
    p_val = float(3.14*d)
#correction factor
    delta = float(d/4)
    Lc = float(L + delta)
if (jk == 1):
    b = float(input("width of fin (w in meters): "))
    t = float(b/2)
    A_val = float(L*b)
    p_val = float(2*(L+b))
#correction factor
    Lc = float(L + t)


print("THE PROGRAM REQUIRES DATA IN SI UNITS & temperatures are in degC")
print("")

# data entry

h_val = float(input("thermal conductivity value of ambient fluid (h): "))
k_val = float(input("thermal conductivity material of fin (k): "))
Ts_val = float(input("temperature of base plate (Ts): "))
Ta_val = float(input("value of ambient temperature (Ta): "))


#calculation
m = np.sqrt((h_val*p_val)/(k_val*A_val))
c1 = float (h_val*p_val*k_val*A_val)
c = np.sqrt(c1)

HeatFlowRate = float(c*(sp.tanh(m*(Lc)))*(Ts_val-Ta_val))

print("")
print("The heat flow rate of fin is: ", HeatFlowRate,"W")

#temperature gradient plotting
x_axis=[]
y_axis=[]
z_axis=[]

for x in np.arange(0,Lc,0.01):
    t1 = float(Ts_val-Ta_val)
    t2 = float(sp.cosh(m*(Lc-x)))
    t3 = float(sp.cosh(m*(Lc)))
    t4 = float(t1*t2)
    tempGrad = float((t4/t3)+Ta_val)
    x_axis.append(x)
    y_axis.append(tempGrad)
    z_axis.append(0)
    print(x,t1,t2,t3,t4,tempGrad)    


plt.title("tempetature-distance plot")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)    
plt.plot(x_axis,y_axis, color='red')
plt.show()
