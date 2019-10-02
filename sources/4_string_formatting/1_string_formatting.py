# Using one argument
name = 'Lala'
print("Hello, %s!" % name)

# Using two or more argument specifier
age = 32
gpa = 3.45
print("""Name: %s
Age: %d olds
GPA: %.2f """ % (name, age, gpa))

gpas = [3.42, 3.43, 3.45]
print("""Name: %s
Age: %s olds
GPAs: %s """ % (name, age, gpas))

one = 1
eight = 8
ten = 10
sixten = 16

print("%d dec = %x or %X hex" % (one, one, one))
print("%d dec = %x or %X hex" % (eight, eight, eight))
print("%d dec = %x or %X hex" % (ten, ten, ten))
print("%d dec = %x or %X hex" % (sixten, sixten, sixten))
