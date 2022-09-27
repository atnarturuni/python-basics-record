


def zero_div_handler_decorator(func):
    def wrapper(*args, **kwargs):
        x, y = args
        if y == 0:
            return None
        return func(*args, **kwargs)
    return wrapper


# decorated_div = zero_div_handler_decorator(div)
@zero_div_handler_decorator
def div(x, y):
    return x / y


print(div(4, 2))
print(div(4, 0))
