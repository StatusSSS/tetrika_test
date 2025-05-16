import inspect
from functools import wraps


def strict(fn):
    sig = inspect.signature(fn)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)

        for name, value in bound.arguments.items():
            expected = fn.__annotations__.get(name)
            if expected is None:
                continue

            if expected is bool:
                if type(value) is not bool:
                    raise TypeError(f"{name} должно быть bool, а не {type(value).__name__}")
            else:
                if type(value) is bool or not isinstance(value, expected):
                    raise TypeError(f"{name} должно быть {expected.__name__}, а не {type(value).__name__}")

        return fn(*args, **kwargs)

    return wrapper


