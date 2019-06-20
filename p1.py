primeNumberList = []
flag = True
for num in range(2, 1000):
    for i in range(2, num):
        if num % i == 0:
            ##print(num, "is not prime!")
            flag = False
            break

    if flag == True:
        primeNumberList.append(num)
    else:
        flag = True


for n in primeNumberList:
    print(n)
    
        
