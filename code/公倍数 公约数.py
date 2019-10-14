def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

a=63
b=27
print(gcd(a,b)) #最大公约数

print(a*b//gcd(a,b)) #最小公倍数