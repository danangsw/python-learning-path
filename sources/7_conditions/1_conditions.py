#- Python uses boolean variable to evaluate conditions.
# Variable assignment is a single equals operator `=`.
# Comparasion operators are using the double equals operator `==`. The "not equals" operator is marked as `!=`.

print("condition #1")
x = 2
print(x == 2)
print(x == 3)
print(x != 2)
print(x > 1)
print(x < 3)

# A statement is evaluated as true if one of the following is correct: 
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
# 2. An object which is not considered "empty" is passed.
#   1. An empty string: "" 
#   2. An empty list: [] 
#   3. The number zero: 0 
#   4. The false boolean variable: False

print("condition #2")
statement = []
other_statement = True

if statement:
    print('statement')
    pass
elif other_statement:
    print('other_statement')
    pass
else:
    print('no_statement')
    pass

print("condition #3")
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")