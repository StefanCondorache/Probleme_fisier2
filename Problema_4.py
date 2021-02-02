def prime(x):
    l_div=[]
    for y in range(1,x+1):
        if x%y==0:
            l_div.append(y)
    if len(l_div)==2 and (1 in l_div) and (x in l_div):
        return True
    else:
        return False
n,nr,l1=int(input(':')),0,[]
for x in range(1,n):
    if prime(x)==True:
        nr+=1
        l1.append(x)
    else:
        continue
print(nr,'\n',l1)