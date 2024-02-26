from collections import deque
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
q = deque()
print(q)

q.append(1)
print(q)

q.append(2)
print(q)

q.appendleft(0)
print(q)

q.pop()
print(q)

q.popleft()
print(q)

for i in range(2,6):
    q.append(i)
print(q)    

q.insert(2,3)
print(q)

q.remove(3)
print(q)


print(q.count(2))


q.extend([6,7,8])
print(q)

q.extendleft([9,10,11])
print(q)

q.rotate(-3)
print(q)

q.reverse()
print(q)

q.clear()
print(q)