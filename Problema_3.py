def fact(x):
    prod=1
    for y in range(1,x+1):
        prod*=y
    return prod
n=int(input(':'))
for x in range(n):
    if sum(list(map(lambda y:fact(int(y)),str(x))))==x:
        print(x)
    else:
        continue