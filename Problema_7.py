n,nr=int(input(':')),0
for x in range(n):
    a=int(input(':'))
    if a>999 and a<10000:
        l1=[int(x) for x in str(a)]
        if l1[0]+l1[1]==l1[2]+l1[3] and l1[2]+l1[3]==13:
            nr+=1
    else:
        break
print(nr)
