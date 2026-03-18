d=1
a=input()
s=0
a=a[::-1]
for i in a:
    s+=int(i)*d
    d*=2
print(s)