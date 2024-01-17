# Incorrect usage of <>
if 5 <> 10:
    print("5 is not equal to 10")

# Incorrect usage of =+ instead of +=
a = 5
b = 10
a += b
a == c
a =+ b
print("Value of a:", a)

# Incorrect usage of \ outside of raw strings
invalid_path = "C:\Users\username\Documents"

# Incorrect usage of __exit__ without type, value, and traceback arguments
class CustomResource:
    def __exit__(self):
        print("Exiting")

# Incorrect usage of __init__ returning a value
class MyClass:
    def __init__(self):
        return 10

# Incorrect usage of break outside of a loop
def break_outside_loop():
    print("This is outside of loop")
    break

# Incorrect usage of except clause just to raise the same issue
try:
    something()
except Exception as e:
    raise e

# Incorrect usage of raising Exception/BaseException
raise Exception("An error occurred")

# Needlessly using pass statement
def my_function():
    pass

# Incorrect usage of return and yield in the same function
def generator_function():
    yield 1
    return 10

# Incorrect usage of self not being the first argument in an instance method
class ExampleClass:
    def method(self, arg1, arg2):
        pass

# Incorrect usage of not re-raising SystemExit
try:
    sys.exit(1)
except SystemExit as e:
    print("Caught SystemExit")
    raise e

# Duplicate code?
try:
    something()
except Exception as e:
    raise e

# Refactored code to eliminate duplication
def calculate_area(shape, *args):
    if shape == "rectangle":
        return args[0] * args[1]
    elif shape == "circle":
        return 3.14 * args[0] * args[0]
    else:
        raise ValueError("Unsupported shape")

def calculate_circumference(shape, *args):
    if shape == "rectangle":
        return 2 * (args[0] + args[1])
    elif shape == "circle":
        return 2 * 3.14 * args[0]
    else:
        raise ValueError("Unsupported shape")