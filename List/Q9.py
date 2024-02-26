# wap to remove duplicates from list

lst = [1,2,3,7,2,1,5,6,4,8,5,4]
n = len(lst)

lst2 = []
print(lst)
for i in lst:
    lst.pop(i)
    lst2.append(i)

print(lst2)

        