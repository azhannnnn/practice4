# Python prog to swap elements in string list

list1 = []

n = int(input("enter the size of list : "))

for i in range(n):
    num = input("Enter the value  : ")
    list1.append(num)

print(list1)    

pos1 = int(input("enter pos1 : ")) - 1
pos2 = int(input("enter pos2 : ")) - 1


list1[pos1] , list1[pos2] = list1[pos2] , list1[pos1]

print(list1)