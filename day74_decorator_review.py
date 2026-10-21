def decorator(func):
    def wrapper():
        print("开工前")
        func
        print("开工后")

    return wrapper


@decorator
def hello():
    print("你好")


# hello = decorator(hello)
hello()
