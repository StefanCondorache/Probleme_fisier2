n=int(input(':'))
list1=list(map(int,str(n)))
list2=sorted(list(map(int,str(n))))
if list1==list2:
    print('DA')
else:
    print('NU')