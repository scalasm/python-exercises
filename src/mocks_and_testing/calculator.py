from functools import wraps

from typing import Any

# The actual logging implementation that we will want to mock
def log_stuff(*args, **kwargs):
    f = args[0]
    args = args[1:]
    print(f"Running {f.__name__}(args={args}, kwargs={kwargs})" )

# function decorator
def audited(function):
    """Logs function execution with name and actual arguments"""

    @wraps(function)
    def audit_method_execution(*args, **kwargs):
        log_stuff( function, *args, **kwargs)
        return function(*args, **kwargs)

    return audit_method_execution

# class-style decorator (useful if you want to keep a state)
class Audited:
    """Auditor class instead of a method, see https://stackoverflow.com/a/63402841/522427"""
    def __init__(self, original_method):
        self.original_method = original_method

    def __get__(self, instance, owner):
        return type(self)(self.original_method.__get__(instance, owner))

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        log_stuff( self.original_method, *args, **kwargs)
        return self.original_method( *args, **kwargs)


class Calculator:
    def __init__(self):
        print( "Calculatore created!" )

    @Audited
    def add(self, a: int, b: int) -> int:
        return a + b 


@Audited
def hello_world(who: str):
    return f"Hello {who}'s world!"


if __name__ == "__main__":
    calculator = Calculator()

    print( calculator.add(2, 2) )

    hello_world("Mario")