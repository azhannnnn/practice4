
# a = 15
# b = 15

# x = lambda a,b : a+b

# print(x(a,b))


# a = "Azhan khan"

# x = list(a)

# print(x)

# print("".join(x))

# print(a[::-1])


# def lowercase_decorator(fun):
#    def wrapper():
#        func = fun()
#        string_lowercase = func.lower()
#        return string_lowercase
#    return wrapper

# # this is executed next
# @lowercase_decorator # this is executed first
# def hello():
#    return 'Hello World'


# print(hello())   # output => [ 'hello' , 'world' ]

a = [10,20,30]
b = [40,50,60]

d = [((x,y) for x in a for y in b)]

def __str__(d):
    return str(d)

print(str(d))