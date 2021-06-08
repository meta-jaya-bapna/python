n = int(input('Enter any number'))
for i in range(1, n):
    if i>100:
        break
    elif i%10==0:
        continue
    else:    
        print(i)
