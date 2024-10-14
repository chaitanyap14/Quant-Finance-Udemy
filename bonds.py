import numpy as np

class ZeroCouponBond:

    def __init__(self, principal, maturity, rate):
        self.principal = principal
        self.maturity = maturity
        self.rate = rate/100

    def present_value(self, x, t):
        return x/(1 + self.rate)**t

    def price_calc(self):
        return self.present_value(self.principal, self.maturity)


class ZeroCouponBondCont:

    def __init__(self, principal, t, rate):
        self.principal = principal
        self.t = t
        self.rate = rate/100

    def present_value(self, x, t):
        return x/np.exp(self.rate*t)

    def price_calc(self):
        return self.present_value(self.principal, self.t)


class CouponBond:

    def __init__(self, principal, coupon, maturity, rate):
        self.principal = principal
        self.coupon = coupon/100
        self.maturity = maturity
        self.rate = rate/100

    def present_value(self, x, t):
        return x/(1 + self.rate)**t

    def coupon_calc(self):
        cash = 0
        for i in range(1,self.maturity+1):
            cash += self.present_value(self.principal*self.coupon, i) 
        return cash

    def principal_calc(self):
        return self.present_value(self.principal, self.maturity)


class CouponBondCont:

    def __init__(self, principal, coupon, t, rate):
        self.principal = principal
        self.coupon = coupon/100
        self.t = t
        self.rate = rate/100

    def present_value(self, x, t):
        return x/np.exp(self.rate*t)

    def coupon_calc(self):
        cash = 0
        for i in range(1, self.t):
            cash += self.present_value(self.principal*self.coupon, i)
        return cash

    def principal_calc(self):
        return self.present_value(self.principal, self.t)


zcbond = ZeroCouponBond(1000, 2, 4)
zcbondcont = ZeroCouponBondCont(1000, 12, 4)
cbond = CouponBond(1000, 10, 3, 4)
cbondcont = CouponBondCont(1000, 10, 15, 4)

print("Price of zero coupon bond: ", zcbond.price_calc())
print("Price of coupon bond: ", cbond.coupon_calc()+cbond.principal_calc())
print(" ")
print("Price of zero coupon bond in a continuous model: ", zcbondcont.price_calc())
print("Price of coupon bond in a continuous model: ", cbondcont.coupon_calc()+cbondcont.principal_calc())
