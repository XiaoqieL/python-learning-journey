def outer(x):
    def inner():
        print(x)

    return inner


f = outer("你好")
g = outer("再见")
f()
g()
