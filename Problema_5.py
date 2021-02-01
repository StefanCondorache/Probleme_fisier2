n,nr=int(input(':')),0
for x in range(n):
    a=int(input(':'))
    if a>99 and a<1000:
        l1=[int(x) for x in str(a)]
        if l1[0]+l1[1]==l1[2] or l1[0]+l1[2]==l1[1] or l1[2]+l1[1]==l1[0]:
            nr+=1
    else:
        break
print(nr)
