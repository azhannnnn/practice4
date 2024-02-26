# Python ways to find length of list

list1 = []
n = int(input("list size  :"))

for i in range(n):
   num = int(input("enter number : "))
   list1.append(num)
print(list1)

# using len function
print(len(list1))

# using naive method
count = 0
for i in list1:
   count = count + 1
print(count)

