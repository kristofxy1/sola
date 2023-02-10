l = 1
a = 0
sps = 0
i = 0.2
s = 1.6/10**8
while l:
    l = int(input("l: ")) / 10**2
    if l == 100:
        break
    u = int(input("u: ")) / 10**3
    r = u / i
    print("R je:", r, "ohm")
    sp = r*s/l
    print(sp)
    sps += sp
    a += 1
print(sps/i)
    
    
