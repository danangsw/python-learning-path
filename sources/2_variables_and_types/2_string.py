# Strings are defined either with a single quote or a double quotes
apostrophes = "Don't worry about apostrophes"
myquote = '"This is quote!"'

print(apostrophes)
print(myquote)

# There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters.
# print('C:\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: foo [OPTIONS]
     -h                 Display this usage message
     -H                 Hostname to connect to
""")

# Simple operators can be executed on numbers and strings
one = 1
two = 2
three = one + two
print(three)

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * "wk" + "land")

longtext = ("Put several strings "
"within parentheses to have "
"them joined together")

print(longtext)

longtext = ("Put several strings \
within parentheses to have \
them joined togethers")

print(longtext)

# Strings can be indexed (subscripted), with the first character having index 0.
string = "Python3"
print(string[0]) # character in position 0
print(string[6]) # character in position 6
print(string[-1]) # last character
print(string[-7]) # 7th last character

print(string[:2]) # characters from position 0 (included) to 2 (excluded)
print(string[:5]) # characters from position 0 (included) to 5 (excluded)
print(string[2:3]) # characters from position 2 (included) to 3 (excluded)
print(string[2:]) # characters from position 2 (included) to the end
print(string[-2:]) # characters from position 2 last (included) to the end

# The built-in function len() returns the length of a string
print(len(longtext))

hello = "Hi"
one, two = 1, 2 # Assignments can be done on more than one variable "simultaneously" on the same line

# Mixing operators between numbers and strings is not supported
print(hello + one + two)