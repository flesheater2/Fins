import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

print("THE PROGRAM REQUIRES DATA IN SI UNITS & temperatures are in degC")
print("")

# data entry
d = float(input("dia of the fin (d): "))
r = float(d/2)
L = l_fin = float(input("length of the fin (L): "))
h_val = float(input("thermal conductivity value of ambient fluid (h): "))
p_val = float(3.14*d)
k_val = float(input("thermal conductivity material of fin (k): "))
A_val = float(3.14*r*r)
Ts_val = float(input("temperature of base plate (Ts): "))
Ta_val = float(input("value of ambient temperature (Ta): "))

#correction factor
delta = float(d/4)
Lc = float(L + delta)
#calculation
m = np.sqrt((h_val*p_val)/(k_val*A_val))
c1 = float (h_val*p_val*k_val*A_val)
c = np.sqrt(c1)

HeatFlowRate = float(c*(sp.tanh(m*(Lc)))*(Ts_val-Ta_val))

print("")
print("The heat flow rate of fin is: ", HeatFlowRate,m,"W")

#temperature gradient plotting
x_axis=[]
y_axis=[]

for x in np.arange(0,Lc,0.01):
    t1 = float(Ts_val-Ta_val)
    t2 = float(sp.cosh(m*(Lc-x)))
    t3 = float(sp.cosh(m*(Lc)))
    t4 = float(t1*t2)
    tempGrad = float(t4/t3)
    x_axis.append(x)
    y_axis.append(tempGrad)
    print(t1)

plt.title("tempetature-distance plot")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)    
plt.plot(x_axis,y_axis, color='red')
plt.show()
