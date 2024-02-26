
n = 5

# for i in range(n):
#     print("+"*i)

# for i in range(n):
#     print(" "*(n-i),"+"*i)

# for i in range(n,0,-1):
#     print(" "*(n-i),"+"*i)

# for i in range(1,n):
#     print(" "*(n-i),"+"*i)

# for i in range(n-1,0,-1):
#     print("+"*i)


k = []
count = 1
for i in range(1,5):
    k.append(i)
    for j in k:
        print(count,end=" ")
        count+=1
    print()    
    