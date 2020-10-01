# 13-Reasons-Why-Hackerearth

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
a, b = b, a
a *= c
b += c 
print(a, b)
