# Python prog to swap two elements in a list


list1 = []
n = int(input("list size  :"))

for i in range(n):
   num = int(input("enter number : "))
   list1.append(num)

print(list1)

pos1=int(input("Pos1:"))-1
pos2=int(input("Pos2:"))-1

list1[pos1],list1[pos2] = list1[pos2],list1[pos1]

print(list1)