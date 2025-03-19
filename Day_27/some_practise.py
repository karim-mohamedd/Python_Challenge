def add_me(*args):
    while args:
        args += args

result = add_me(1,2,3,4)
print(result)