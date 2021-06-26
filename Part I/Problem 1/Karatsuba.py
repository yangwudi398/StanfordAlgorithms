# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:25:43 2021

@author: yangw
"""

def multiply(x, y):
    n = len(x)
    
    if n == 1:
        return str(int(x) * int(y))
    
    a = x[:n//2]
    b = x[n//2:]
    c = y[:n//2]
    d = y[n//2:]
    
    ac = multiply(a, c)
    ad = multiply(a, d)
    bc = multiply(b, c)
    bd = multiply(b, d)
    adbc = add(ad, bc)
    
    return add(tenPower(ac, n), tenPower(adbc, n//2), bd)
    
def add(x, *ys):
    res = x
    
    for y in ys:
        new = ''
        
        if len(res) < len(y):
            temp = res
            res = y
            y = temp
        
        carry = 0
        pr = len(res) - 1
        py = len(y) - 1
        
        while py >= 0:
            curr = int(res[pr])+ int(y[py]) + carry
            digit = curr % 10
            carry = curr // 10
            new = str(digit) + new
            pr -= 1
            py -= 1
            
        while carry > 0 and pr >= 0:
            curr = int(res[pr]) + carry
            digit = curr % 10
            carry = curr // 10
            new = str(digit) + new
            pr -= 1
            
        if carry > 0:
            new = str(carry) + new
            
        if pr >= 0:
            new = res[:pr + 1] + new
            
        res = new
            
    return res

def tenPower(x, p):
    for i in range(0, p):
        x += '0'
    return x

x = '3141592653589793238462643383279502884197169399375105820974944592'
y = '2718281828459045235360287471352662497757247093699959574966967627'
res = multiply(x, y)
print(res)