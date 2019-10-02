def my_function_one():
    print("Greeting from my_function_one")
    pass

def my_function_with_args(name, age):
    print("Hi, %s your age is %d years old" % (name, age))
    pass

def sum_numbers(x, y):
    return x + y

my_function_one()
my_function_with_args("John", 39)
a = sum_numbers(1, 2)
print(a)
