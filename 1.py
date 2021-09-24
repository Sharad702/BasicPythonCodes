n=int(input("Enter the range of number:"))
sum=0
p=9
for i in range(1,n+1):
     sum += p
     print (p,end=" ")
     p=(p*10)+9
print("\nThe sum of the series = ",sum)