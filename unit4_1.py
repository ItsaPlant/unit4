# def addition(a, b):
#     return a + b

# print(addition(2, 4))

# a = 1

# def scope_demo():
#     a = 2
#     return a

# print(a)

# def none():
#     pass

# print(type(none()))

# def shopping(items, payment = "card", shop = "local"):
#     pass
# items = ["jajko", "majonez"]
# print(shopping(items, "market"))

# def fun_d( arg_1, arg_2):
#     pass

# def fun_p(arg_1, arg_2, /):
#     pass

# def fun_k(*,arg_1, arg_2):
#     pass

# fun_p(arg_1=3, arg_2=3)

def all_of(*args, **kwargs):
    print(len(args))
    print(len(kwargs))

x = all_of(1, 2, 3, 4, 4, 5, s=1, d="c")
print(x)

help(print())