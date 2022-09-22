def sort(num):
    for i in range (5):
        minpose=i
        for j in range  (i,6):
            if num[j]<num[minpose]:
                print((num[minpose],num[j]))
                minpose=j
                
        temp=num[i]
        num[i]=num[minpose]
        num[minpose]=temp

num = [ 2, 1, 10, 23, 4, 6 ]

sort(num)

print(num)
###