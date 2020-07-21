import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sympy as syp

C_a = 1.0
C_b = 0.5
x = syp.symbols("x")
K_a = syp.symbols("K_a")

real = x * (C_b + x) / (C_a - x) - K_a
approxi = x * C_b / C_a - K_a

K_a_space = np.linspace(0,1,1000,)[1:]
x_real_space = np.array([])
x_approxi_space = np.array([])

for Kas in K_a_space:
    real_ks = real.subs(K_a,Kas)
    approxi_ks = approxi.subs(K_a,Kas)
    x_real = syp.solve(real_ks,x)[1]
    x_approxi = syp.solve(approxi_ks,x)[0]
    x_real_space = np.append(x_real_space,[float(x_real)])
    x_approxi_space = np.append(x_approxi_space,[float(x_approxi)])



x_real_space = -np.log10(x_real_space)
x_approxi_space = -np.log10(x_approxi_space)
x_delta_space = x_real_space - x_approxi_space

plt.subplot(2,1,1)
plt.plot(K_a_space, x_real_space)
plt.plot(K_a_space, x_approxi_space)

plt.subplot(2,1,2)
plt.plot(K_a_space,x_delta_space)

print(x_approxi_space)
print(x_real_space)

plt.show()
#산해리상수의 증가에 따른 근사식과 실제식이 구한 pH값의 차이

