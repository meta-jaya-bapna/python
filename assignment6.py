print('Enter any number')
n = int(input())
primeFlag = True
for i in range(2, n-1):
    if n%i == 0:
        primeFlag = False
        break
if(primeFlag):
    print("Prime number")
else:
    print("Not a prime number")
