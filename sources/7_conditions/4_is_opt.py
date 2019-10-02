# Unlike the double equals operators `==`, the `is` opererator does not match the values of variables, but the instances it themselves.
x = [1, 2, 3]
y = [1, 2, 3]
z = x

if x is y:
    print("x is y")
    pass
if x is z:
    print("x is z")
    pass
if x == y:
    print("x == y")
    pass
if y == z:
    print("y == z")
    pass