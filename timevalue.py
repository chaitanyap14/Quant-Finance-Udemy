import numpy as np

def future_val_discrete(pv, r, u, y):
    return pv*(1 + r/u)**(u*y)

def present_val_discrete(fv, r, u, y):
    return fv*(1+r/u)**(-u*y)

def future_val_cont(pv, r, t):
    return pv*np.exp(r*t)

def present_val_cont(fv, r, t):
    return fv/np.exp(r*t)

print(future_val_discrete(100, 0.02, 1, 5))
print(present_val_discrete(110.408, 0.02, 1, 5))
print(future_val_cont(100, 0.02, 12))
print(present_val_cont(127.125, 0.02, 12))
