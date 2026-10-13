import numpy as np

k = 500
forces = np.arange(0,101,10)
x = forces/k
forces_above = forces[forces>0.1*k]

print(f"Forces in N = {forces}")
print(f"Spring Constant N/m = {k}")
print(f"Extensions in m = {x}")
print(f"Maximum Extension in m = {np.max(x)}")
print(f"Minimum Extension in m = {np.min(x)}")
print(f"Mean or Average Extension in m = {np.mean(x)}")
print(f"Standard Deviation = {np.std(x):.4f}")
print(f"Variance = {np.var(x):.4f}")
print(f"Forces Greater than 0.1m Extensions in N = {forces_above}")