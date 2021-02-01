n=int(input(':'))
list1=[int(x) for x in str(n) if int(x)%2==0]
list2=[int(x) for x in str(n) if int(x)%2!=0]
print('numere pare:',len(list1))
print('numere impare:',len(list2))