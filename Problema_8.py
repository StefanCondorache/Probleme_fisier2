n,nr,ind=int(input(':')),'',0
l1=sorted(list(map(lambda x:int(x),str(n))))
for x in l1:
    if x==0:
        ind+=1
del(l1[0:ind])
l1.insert(1,'0'*ind)
for x in l1:
    nr+=str(x)
print(nr)