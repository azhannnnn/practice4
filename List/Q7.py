# Wap to sum all the items

n = int(input("enter the size of list : "))

lst = []
sum = 0

for i in range(n):
    num = int(input("Enter elements : "))
    lst.append(num)
    sum = sum + lst[i]

print(sum)